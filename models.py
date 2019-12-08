from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy.orm import backref, relationships


Base = declarative_base()


class Disease(Base):
    __tablename__ = 'diseases'
    id = Column(Integer, Sequence('diseases_id_seq'), primary_key=True)
    IDC_10 =  Column(String(15))
    disease = Column(String(256))

     def __repr__(self):
        return "<Disease(IDC_10='%s', disease='%s')>" % (
                                self.IDC_10, self.disease)

class ClassName(object):
    """docstring for ."""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
