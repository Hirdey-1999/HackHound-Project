from sqlalchemy.orm import Session

from models import *
from Schemas import *
def create_user_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return