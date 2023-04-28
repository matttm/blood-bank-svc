

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..services.utility_service import UtilityService

env_vars = {
    'DB_HOST': None,
    'DB_PORT': None,
    'DB_NAME': None,
    'DB_USERNAME': None,
    'DB_PASSWORD': None
}
UtilityService.populate_config_from_environment(env_vars)

engine = create_engine(
    'mysql+pymysql://{user}:{pword}@{host}:{port}/{name}'.format(
        user=env_vars['DB_USERNAME'], pword=env_vars['DB_PASSWORD'], host=env_vars['DB_HOST'], port=env_vars['DB_PORT'], name=env_vars['DB_NAME']
        )
        )

Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

session = Session()
