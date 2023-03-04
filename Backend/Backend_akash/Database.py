from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

SQL_ALCHEMY_URL = ("postgresql://akash:QA7rCKUzX0PrPpmM4QRJpw@dour-snorter-2446.7s5.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

engine = create_engine(
    SQL_ALCHEMY_URL
)
session = sessionmaker(autoflush=False, autocommit=False,bind=engine)

Base = declarative_base()

