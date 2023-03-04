from sqlalchemy.orm import relationship
from sqlalchemy import Integer,Boolean,Column,ForeignKey,String,Float,ARRAY,ClauseList,Tuple

from Database import Base

class User(Base):
    __tablename__ = "Userbase"
    id = Column(Integer,primary_key=True,default=0)

class Restaurant(Base):
    __tablename__ = "Restaurant"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,default="")
    Address = Column(String,default="")
    Phone = Column(Integer,nullable=False)


class Menu(Base):
    __tablename__ = "Menu"
    id = Column(Integer, primary_key=True, index=True)
    Rest = Column(Integer, ForeignKey("Restaurant.id"))
    name = Column(String,default="")
    Ingredients = Column(String,nullable=True)
    cost = Column(Integer,default=0)


class Order(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, index=True)
    users = Column(Integer , ForeignKey("Userbase.id"))
    Total_cost = Column(Integer,default=0)
    Total_items = Column(Integer,default=0)
    # All the table User Fields

class Nutrition_level(Base):
    __tablename__ = "Nutrition"
    id = Column(Integer, primary_key=True, index=True)
    food = Column(Integer, ForeignKey("Menu.id"))
    Protein = Column(Integer,default=0)
    Carbohydrates = Column(Integer,default=0)
    Fats = Column(Integer, default=0)
    Sugar = Column(Integer, default=0)
    # All the table User Fields


class cart(Base):
    __tablename__ = "Cart"
    id = Column(Integer,primary_key=True,index=True)
