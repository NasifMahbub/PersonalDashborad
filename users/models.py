# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser, models.Model):
    pass
    # add additional fields in here
    #user_id = models.IntegerField(primary_key= True)
    contact_no = models.CharField(max_length=20, default = "")
    image = models.ImageField(upload_to='profile_image', blank=True)
    __name__='CustomUser'
    
    def __str__(self):
        return self.username


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey
from sqlalchemy import Sequence

engine = create_engine('sqlite:///foo.db')
#engine = create_engine(settings.DB_CONNECTION_URL,)
""" Session = sessionmaker(bind = engine)
session = Session() """

Base = declarative_base()

class SQLUser(Base):
    __tablename__ = 'users'
    sqluser_id = Column(Integer(), Sequence('user_id_seq'), primary_key = True) 
    user_name = Column(String(150), unique = True)
    email_adress = Column(String(255), nullable = False)
    first_name = Column(String(60))
    last_name = Column(String(60))
    contact_no = Column(String(20))

class SQLCustomUser(Base):
    __tablename__ = 'sqlusers'
    sql_id = Column(Integer(), Sequence('user_id_seq'), primary_key = True) 
    user_name = Column(String(150), ForeignKey('CustomUser.username'))
    email_address = Column(String(255), nullable = False)
    first_name = Column(String(60))
    last_name = Column(String(60))
    contact_no = Column(String(20))
    
Base.metadata.create_all(engine)








