from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Disease, Base

# Create database
engine = create_engine("postgresql://kekik:gizli@localhost/sqlalchemy_aid")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

async def init_db():
    from models import Disease
    Base.metadata.drop_all(bind=engine)


    db_session.commit()
