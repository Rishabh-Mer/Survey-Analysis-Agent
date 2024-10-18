import os
import uvicorn
import requests
from dotenv import load_dotenv
from fastapi import FastAPI

from langserve import add_routes
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_community.llms import huggingface_hub
from langchain.docstore.document import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from langchain_community.llms import ollama
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

from data_preprocess import preprocess, generate_text_block, read_file


load_dotenv()

# api token for huggingface
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# Name of model used for embedding
embedding_model_name = "sentence-transformers/all-mpnet-base-v2"

# initializing fastapi app
app = FastAPI(
    title="Survey Analysis Server",
    version="1.0",
    description="Survey Analysis Agent using RAG"
)

# prompt template
template = """
    You are a survey data analyst expert, provide valueable insights of the survey data and answer the questions
    If the question cannot be answered using the information provided answer with "I don't know"
    
    <context>
    Survey data / Context: {context}
    </context>

    Question: {input}
"""

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
output_parser = StrOutputParser()

# Preprocessing dataframe and generating text for embedding
df = read_file("./Sustainability Research Results.xlsx")
cleaned_df = preprocess(df)
text_block = generate_text_block(cleaned_df)
print(f"Text Block: ", text_block)

# Converting the text block to Document
document = [Document(page_content=text) for text in text_block]
# Storing data for easy retrivals
vector_store = Chroma.from_documents(documents=document, embedding=embedding_model)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["context", "input"],
    template=template
)
# Retriever to get top 5 result based on similarity
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={'k': 5})

# LLM 
llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

entry_point_chain = RunnableParallel(
    {"context": retriever, "input": RunnablePassthrough()}
)

# LLM Chain
llm_chain = entry_point_chain | prompt | llm | output_parser

# Langserve to return the result on specified localhost
add_routes(app, llm_chain, path="/analysis")

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8000)













