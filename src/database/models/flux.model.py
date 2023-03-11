
from sqlalchemy import Column, String, Integer, Date

from base import Base


class Flux(Base):
    __tablename__ = 'FLUX'

    flux_id = Column('FLUX_ID', Integer, primary_key=True)
    flux_type = Column('FLUX_TYPE', String)
    donor_id = Column('DONOR_ID', Integer)

    def __init__(self, flux_id, flux_type, donor_id):
        self.flux_id = flux_id
        self.flux_type = flux_type
        self.donor_id = donor_id
