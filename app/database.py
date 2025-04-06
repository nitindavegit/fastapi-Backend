from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from  psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# while True :  
#     try:
#         conn = psycopg2.connect(host = 'localhost',database = 'fastapi', user =  'postgres', password = 'password321',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was successful')
#         print("Database connect ho gya h bhai !!")
#         break

#     except Exception as error:
#         print('Connecting to database failed')
#         print("Connection nhi hua h bhai database k saath")
#         print('Error', error)
#         time.sleep(2)