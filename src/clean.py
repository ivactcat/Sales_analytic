import pandas as pd
import numpy as np

def dollars_float(dataframe,col):
    # Replace the dollar symbol "$" in the specified column
    dataframe[col]= dataframe[col].str.replace("$","").astype(float)
    return dataframe # Return the modified DataFrame