from sqlalchemy import create_engine

from config import URL_DATABASE

db = create_engine(URL_DATABASE)