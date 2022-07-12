from mimetypes import init
from pyexpat import model
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:////tmp/teste.db")
db_session = scoped_session(sessionmaker(autocommit= False, autoflush=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()

def init_db():
    import crud
    base.metadata.create_all(bind=engine)
