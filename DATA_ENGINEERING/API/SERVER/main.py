import os
import pandas as pd
from fastapi import FastAPI

# This file creates a local REST API on local host 8000
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
OUTPUT_DIR = os.path.join(BASE_DIR, 'CLEANED_DATA')

dataset = os.path.join(OUTPUT_DIR, 'Amazon-Flex_CDF.csv')

app = FastAPI()

@app.get('/')

def read_root():
    print(OUTPUT_DIR)
    return {"Hello": "World"}

@app.get("/cleaned-data")

def read_cleaned_data():
    df = pd.read_csv(dataset)
    return df.to_dict(orient='index')



