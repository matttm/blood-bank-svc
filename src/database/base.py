

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys

env_vars = [
    'DB_HOST': None,
    'DB_PORT': None,
    'DB_NAME'; None,
    'DB_USER': None,
    'DB_PASSWORD': None
]
for var in env_vars:
    tmp = os.environ.get(var)
    if tmp is None:
        print(f'Error: {tmp} is not defined')
        sys.exit()
    env_vars[var] = tmp

engine = create_engine(f'mysql://{env_vars['DB_USER']}:{env_vars['DB_PASSWORD']}@{env_vars['DB_HOST']}:{env_vars['DB_PORT']}/{env_vars['DB_NAME']}')
Session = sessionmaker(bind=engine)

Base = declarative_base()
