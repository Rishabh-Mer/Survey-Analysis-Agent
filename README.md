# Survey-Analysis-Agent
A survey analysis agent using LLama3.1

Tech Stack:
- Python
- FastAPI
- Streamlit (Frontend)
- Langchain (LLM and RAG)

File Structure
- app.py: fastapi server with langchain
- client.py: Streamlit UI
- data_processing.py: data preprocessing functions

### Installation
---
- Create Python env
    * ```conda create -n env_name python=3.10.15```
    * (if you don't have anaconda here the [link](https://www.anaconda.com/download/success))

- conda activate env_name
- Navigate to the required folder
    - ```pip install -r requirements.txt```

---

### Run Code

### Step 1:
- Edit given ```.env``` file
    - add huggingface api token

#### Step 2:
- Install Ollama (library to run LLM locally)
    - [link](https://ollama.com/)
- After installation open terminal and run
    - ```ollama run llama3.2```

#### Step 3:
- Navigate to the required folder
    - Open 2 terminals
        - run terminal 1: ```python3 app.py```
        - run terminal 2: ```streamlit run client.py ```

    - Click on the link generated on **Terminal 2**
        - http://localhost:8501

    - Type your question on textbox and model will generate and display the result.

---

