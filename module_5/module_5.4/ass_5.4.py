import pandas as pd
from sqlalchemy import create_engine

#pass column names as argument
column = [
    "Names", 
    "Mathematics", 
    "English", 
    "Civics", 
    "Physics"
    ]

data = pd.read_csv("scores_waec.csv", names = column)

engine = create_engine("postgresql+psycopg2://postgres:datafreak@localhost:5432/demo_db")

data.to_sql("scores_waec", engine, index = False)

