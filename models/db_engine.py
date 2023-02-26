import sqlalchemy as sqlalchemy
from db import metadata, DATABASE_URL

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)