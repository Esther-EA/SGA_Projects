import pandas as pd
from sqlalchemy import create_engine

#pass column names as argument
column ="Names","Mathematics", "English","Civics","Physics"

data = pd.read_csv("scores_waec.csv", file = column)

