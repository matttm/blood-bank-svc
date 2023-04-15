
from sqlalchemy import Column, String, Integer, Date

from ..base import Base


class Donor(Base):
    __tablename__ = 'DONOR'

    donor_id = Column('DONOR_ID', Integer, primary_key=True)
    first_name = Column('FIRST_NAME', String)
    last_name = Column('LAST_NAME', String)
    blood_type = Column('BLOOD_TYPE', String)
    email = Column('EMAIL', String, nullable=True)
    created_at = Column('CREATED_AT', Date, nullable=True)
    updated_at = Column('UPDATED_AT', Date, nullable=True)

    def __init__(self, fname, lname, blood_type, email):
        self.first_name = fname
        self.last_name = lname
        self.blood_type = blood_type
        self.email = email
