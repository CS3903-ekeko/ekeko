from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Manager:
    Base = declarative_base()
