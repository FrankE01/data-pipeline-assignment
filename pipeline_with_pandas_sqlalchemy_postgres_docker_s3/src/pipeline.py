import os
from os import path
import pandas as pd
from sqlalchemy import create_engine

data_dir = path.dirname(path.dirname(path.abspath(__file__)))+"/data/"

companies = [d for d in os.listdir(data_dir) if os.path.isdir(path.join(data_dir,d))]

for company in companies:

    engine = create_engine(f"postgresql+psycopg2://postgres:postgres@db/{company}", echo=True)

    files = [f for f in os.listdir(path.join(data_dir,company)) if f[-4:]==".csv"]
    
    for file in files:
        df = pd.read_csv(path.join(data_dir,company,file))
        df_cleaned = df.dropna()
        df_cleaned.to_sql(file[:-4], engine, index=False)

