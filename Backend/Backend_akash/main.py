from typing import List
from fastapi import Depends, FastAPI,HTTPException,Request
from sqlalchemy.orm import Session
from models import *
from Database import session, engine
from twilio.rest import Client

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.post('/order')
async def order(session,info:Request):
    req_info = await info.json()
    #store Order details of user
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

@app.get('/orderdetails/<id:int>')
async def Orderdetails():
    #Show order details
    pass
@app.post('/Users')
async def Users(session,info:Request):
    # update data remains
    req_info = await info.json()
    print("Data get")
    obj = User(
        id=0
    )
    session.add(obj)
    return {
        "status": "SUCCESS",
        "data": req_info
    }
    # Use a breakpoint in the code line below to debug your script.

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
