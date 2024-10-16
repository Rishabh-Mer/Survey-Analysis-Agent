import pandas as pd


def read_file(filepath:str):
    
    df = pd.read_excel(filepath)
    return df


def rename_columns(df:pd.DataFrame):
    
    last_col = None
    
    updated_column = []
    
    for col in df.columns:
        if col.startswith("Column"):
            updated_column.append(last_col)
        else:
            updated_column.append(col)
            last_col = col
            
    return updated_column
    
    
def preprocess(df:pd.DataFrame):
    
    df = pd.read_excel("./Sustainability Research Results.xlsx")
    
    df.dropna(how="all", axis=1, inplace=True)
    df.dropna(how="all", axis=0, inplace=True)
    
    df.replace(" ", float("NaN"),inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    
    df.columns = ['Unnamed' if str(col).startswith(' ') else col for col in df.columns]
    # Renaming unnamed columns
    df.columns = [f'Column_{i+1}' if 'Unnamed' in str(col) else col for i, col in enumerate(df.columns)]
    
    df.rename(columns={'Column_1': 'Demographics'}, inplace=True)
    
    # renaming named "Column" 
    df.columns = rename_columns(df)
    
    return df


def generate_text_block(df:pd.DataFrame):
    
    text_blocks = []
    
    # Iterate over rows
    for index, row in df.iterrows():
        block = []
        for col_name, value in row.items():
            if pd.notna(value):
                block.append(f"{col_name}: {value}")
        
        # Join the non-NaN values into a single block of text
        if block:
            text_blocks.append(" | ".join(block))
    
    return text_blocks



    
    
    
    
    
    
    
    
    
    

    
    
    
    
    