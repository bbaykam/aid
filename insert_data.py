from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.users import Users

# Create database
engine = create_engine("postgresql://kekik:gizli@localhost/sqlalchemy_aid")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Base = declarative_base()
# Base.query = db_session.query_property()
session = db_session()

basar = Users("cem", "mert", "1981-03-18", "male", "cm@gmail.com", "55xxx5", )

session.add(basar)

session.commit()





# async def init_db():
#     from users import Users
#     #Base.metadata.drop_all(bind=engine)
#
#
#     db_session.commit()
