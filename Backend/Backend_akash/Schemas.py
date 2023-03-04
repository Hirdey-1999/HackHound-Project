from typing import Optional,List
from pydantic import BaseModel

class OrderBase(BaseModel):
    id: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    users: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
