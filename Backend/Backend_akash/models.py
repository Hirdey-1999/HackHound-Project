from sqlalchemy.orm import relationship
from sqlalchemy import Integer,Boolean,Column,ForeignKey,String,Float

from .Database import Base

class User(Base):
    __tablename__ = "Userbase"
    # All the table User Fields
    pass

class Restaurant(Base):
    __tablename__ = "Restaurant"
    # All the table User Fields
    pass

class Menu(Base):
    __tablename__ = "Menu"
    Rest = Column(Integer , ForeignKey("Restaurant.id"))
    # All the table User Fields

class Order(Base):
    __tablename__ = "Orders"
    users = Column(Integer , ForeignKey("User.id"))
    # All the table User Fields

class Nutrition_level(Base):
    __tablename__ = "Nutrition"
    food = Column(Integer , ForeignKey("Menu.id"))
    # All the table User Fields

#Bfu1-xjsoAHXcDS0jTiHEQ