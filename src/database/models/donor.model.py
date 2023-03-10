
from sqlalchemy import Column, String, Integer, Date

from base import Base


class Donor(Base):
    __tablename__ = 'DONOR'

    donor_id = Column('DONOR_ID', Integer, primary_key=True)
    first_name = Column('FIRST_NAME', String)
    last_name = Column('LAST_NAME', String)
    blood_type = Column('BLOOD_TYPE', String)

    def __init__(self, fname, lname, blood_type):
        self.first_name = fname
        self.last_name = lname
        self.blood_type = blood_type
