
from sqlalchemy import Column, String, Integer, Date

from base import Base


class Transaction(Base):
    __tablename__ = 'TRANSACTION'

    transaction_id = Column('TRANSACTION_ID', Integer, primary_key=True)
    transaction_type = Column('TRANSACTION_TYPE', String)
    donor_id = Column('DONOR_ID', Integer)

    def __init__(self, transaction_id, transaction_type, donor_id):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.donor_id = donor_id
