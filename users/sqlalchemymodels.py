from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey
from sqlalchemy import Sequence

engine = create_engine('sqlite:///db.sqlite3')
#engine = create_engine(settings.DB_CONNECTION_URL,)
""" Session = sessionmaker(bind = engine)
session = Session() """

Base = declarative_base()

class SQLUser(Base):
    __tablename__ = 'users'
    sqluser_id = Column(Integer(), Sequence('user_id_seq'), primary_key = True) 
    user_name = Column(String(150), unique = True)
    email_address = Column(String(255), nullable = False)
    first_name = Column(String(60))
    last_name = Column(String(60))
    contact_no = Column(String(20))
    image_url = Column(String(512))
    
Base.metadata.create_all(engine)
