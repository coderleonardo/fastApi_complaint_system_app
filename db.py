import databases
import sqlalchemy
import urllib.parse
from decouple import config


URL_PARSE = urllib.parse.quote_plus(config('DB_PASSWORD'))
DATABASE_URL = f"postgresql://{config('DB_USER')}:{URL_PARSE}@localhost:{config('DB_PORT')}/{config('DATABASE')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


