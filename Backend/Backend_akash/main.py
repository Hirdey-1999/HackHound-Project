from typing import List
from fastapi import Depends, FastAPI,HTTPException
from sqlalchemy.orm import Session
from models import *
from Database import session, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
