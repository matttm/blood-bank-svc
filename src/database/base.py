

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

engine = create_engine(
    'mysql://{user}:{pword}@{host}:{port}/{name}'.format(
        user=env_vars['DB_USER'], pword=env_vars['DB_PASSWORD'], host=env_vars['DB_HOST'], port=env_vars['DB_PORT'], name=env_vars['DB_NAME']
        )
        )

Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.reflect()
