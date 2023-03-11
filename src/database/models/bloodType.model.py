
from sqlalchemy import Column, String

from base import Base


class BloodType(Base):
    __tablename__ = 'BLOOD_TYPE'

    blood_type_id = Column('BLOOD_TYPE_ID', String, primary_key=True)
    blood_type_desc = Column('BLOOD_TYPE_DESC', String)

    def __init__(self, blood_type_id, blood_type_desc):
        self.blood_type_id = blood_type_id
        self.blood_type_desc = blood_type_desc
