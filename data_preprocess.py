import pandas as pd
from typing import List


def read_file(filepath:str) -> pd.DataFrame:
    
    """
    This function read the excel file and returns pandas dataframe
    
    Parameters
    ----------
    filepath: str
              Location of the file
    
    Returns
    -------
    pd.Dataframe
        Pandas DataFrame
    """
    
    df = pd.read_excel(filepath) 
    return df


def rename_columns(df:pd.DataFrame) -> List[str]:
    
    """
    This function returns new column names
    if the column name starts with "Column"
    the function replaces with previous non
    "Column" name
    
    Parameters
    ----------
    df: pd.DataFrame
        Pandas Dataframe object
        
    Returns
    -------
    List[str]
        List of new column names which can be renamed
    
    """
    
    # Last Column 
    last_col = None
    
    updated_column = []
    
    for col in df.columns:
        if col.startswith("Column"):
            updated_column.append(last_col)
        else:
            updated_column.append(col)
            last_col = col
            
    return updated_column
    
    
def preprocess(df:pd.DataFrame) -> pd.DataFrame:
    
    """
    
    This function perform data preprocessing on dataframe
    
    Parameters:
    ----------
    df: pd.DataFrame
        Pandas Dataframe object
        
    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe
    
    """
    
    # drop all null values from rows and columns
    df.dropna(how="all", axis=1, inplace=True)
    df.dropna(how="all", axis=0, inplace=True)
    
    # replace empty string from column to NaN and dropping them
    df.replace(" ", float("NaN"),inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    
    # Renaming empty string columns
    df.columns = ['Unnamed' if str(col).startswith(' ') else col for col in df.columns]
    # Renaming all unnamed columns
    df.columns = [f'Column_{i+1}' if 'Unnamed' in str(col) else col for i, col in enumerate(df.columns)]
    
    df.rename(columns={'Column_1': 'Demographics'}, inplace=True)
    
    # renaming named "Column" 
    df.columns = rename_columns(df)
    
    return df


def generate_text_block(df:pd.DataFrame) -> List[str]:
    
    """
    This function returns list of all non nan values in
    column name : value format
    
    Parameters: 
    -----------
    df: pd.DataFrame
        Pandas Dataframe object
        
    Returns:
    --------
    List[str]
        List containing all the non values, represented with column name and its value

    """
    
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



    
    
    
    
    
    
    
    
    
    

    
    
    
    
    