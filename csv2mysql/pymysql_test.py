from os import terminal_size
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from setting_db import db, file_path

df = pd.read_csv(file_path)

df.columns = df.keys()

# use sqlalchemy
engine = create_engine(f"mysql+pymysql://{db.id}:{db.pw}@{db.ip}:3306/{db.name}?charset=utf8", encoding = "utf-8")
connect = engine.connect()
df.to_sql(name = db.table, con = engine, if_exists = 'append', index = False, chunksize = 10000)
connect.close()
