from sqlalchemy import Column, Date, ForeignKey, Integer, String, func, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy.orm import backref, relationships


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('diseases_id_seq'), primary_key=True)
    first_name = Column(String(63), nullable=False)
    last_name = Column(String(63), nullable=False)
    birth_date = Column(Date(), nullable=False)
    gender = Column(Enum('male', 'female'), nullable=False)
    email = Column(String(63), nullable=False, unique=True)
    password = Column(String(63), nullable=False)
    citizen_id = Column(String(63), nullable=True)



    def __init__(self, first_name, last_name, birth_date, gender, email, password, citizen_id=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.email = email
        self.password = password
        self.citizen_id = citizen_id

basar = Users("basar", "baykam", "1971-03-18", "male", "bs@gmail.com", "12345")
