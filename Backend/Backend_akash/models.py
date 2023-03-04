from sqlalchemy.orm import relationship
from sqlalchemy import Integer,Boolean,Column,ForeignKey,String,Float

from Database import Base

class User(Base):
    __tablename__ = "Userbase"
    id = Column(Integer,primary_key=True,index=True)
    # All the table User Fields
    pass

class Restaurant(Base):
    __tablename__ = "Restaurant"
    id = Column(Integer, primary_key=True, index=True)
    # All the table User Fields
    pass

class Menu(Base):
    __tablename__ = "Menu"
    id = Column(Integer, primary_key=True, index=True)
    Rest = Column(Integer , ForeignKey("Restaurant.id"))
    # All the table User Fields

class Order(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, index=True)
    users = Column(Integer , ForeignKey("User.id"))
    # All the table User Fields

class Nutrition_level(Base):
    __tablename__ = "Nutrition"
    id = Column(Integer, primary_key=True, index=True)
    food = Column(Integer , ForeignKey("Menu.id"))
    # All the table User Fields


#QA7rCKUzX0PrPpmM4QRJpw