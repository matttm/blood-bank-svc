
from sqlalchemy import Column, String

from base import Base


class FluxType(Base):
    __tablename__ = 'FLUX_TYPE'

    flux_type_id = Column('FLUX_TYPE_ID', String, primary_key=True)
    flux_type_desc = Column('FLUX_TYPE_DESC', String)

    def __init__(self, flux_type_id, flux_type_desc):
        self.flux_type_id = flux_type_id
        self.flux_type_desc = flux_type_desc
