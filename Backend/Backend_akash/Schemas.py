# from typing import List, Optional
#
# from pydantic import BaseModel
#
#
# class ItemBase(BaseModel):
#     id: int
#     #description: Optional[str] = None
#
#
# class ItemCreate(ItemBase):
#     id: int
#
#
# class Items(ItemBase):
#     #owner_id: int
#
#     class Config:
#         orm_mode = True
