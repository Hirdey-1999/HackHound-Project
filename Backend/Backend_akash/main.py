
from fastapi import Depends, FastAPI,HTTPException,Request
from models import *
from math import floor
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from models import Account
from twilio.rest import Client


app = FastAPI()



@app.post('/order')
async def order(session,info:Request):
    req_info = await info.json()
    print("working")
    obj = Order(
        id=req_info[2]
    )
    session.add(obj)
    print("Added")
    client = Client('AC650ee5c9f0a1d51c072cd9c6ad024d75', 'f503be39f9c13638fdc0d29ae7fba7ba')
    no = '+919910838498'
    # Restaurant number
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="New Order Recieved",
        to='whatsapp:' + no
    )
    run_transaction(session,
                    lambda s: create_accounts(s, 100))
@app.get('/orderdetails/<id:int>')
async def Orderdetails():
    #Show order details
    pass
@app.post('/Users')
def Users(session,info:Request):
    #create_user_item
    req_info = info.json()
    obj = User(
        id=req_info['idd']
    )
    obj.add()

    return {
        "status": "SUCCESS",
        "data": obj
    }
    # # Use a breakpoint in the code line below to debug your script.

@app.patch('/OrderUpdates')
async def Updates(session,info:Request):
    # update data remains
    req_info = await info.json()
    # Use a breakpoint in the code line below to debug your script.
    if req_info['status']=='Processing':
        client = Client('AC650ee5c9f0a1d51c072cd9c6ad024d75', 'f503be39f9c13638fdc0d29ae7fba7ba')
        no = '+919910838498'
        # customer number
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="Order Under Processing",
            to='whatsapp:' + no
        )
    if req_info['status']=='Completed':
        client = Client('AC650ee5c9f0a1d51c072cd9c6ad024d75', 'f503be39f9c13638fdc0d29ae7fba7ba')
        # msg = req_info['first_name'] + '\n' + req_info['last_name'] + '\n' + req_info['lat'] + '\n' + req_info['long']
        no = '+919910838498'
        # customer number
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="Your order has been cooked",
            to='whatsapp:' + no
        )
    obj = Order(
        status=req_info['status']
    )
    session.copy(obj)
    return {
        "status": "SUCCESS",
        "data": req_info
    }
    #

def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)

if __name__ == '__main__':
    # run_transaction(Users(0,session))
    seen_account_ids = []

    SQL_ALCHEMY_URL = ("postgresql://akash:QA7rCKUzX0PrPpmM4QRJpw@dour-snorter-2446.7s5.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

    engine = create_engine(
        SQL_ALCHEMY_URL.replace("postgresql://", "cockroachdb://")
    )
    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))
    run_transaction(sessionmaker(bind=engine),
                    lambda s: Users(s, 100))