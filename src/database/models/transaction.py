
from sqlalchemy import Column, String, Integer, Date, text

from base import Base


class Transaction(Base):
    __tablename__ = 'TRANSACTION'

    transaction_id = Column('TRANSACTION_ID', Integer, primary_key=True)
    transaction_type = Column('TRANSACTION_TYPE', String)
    blood_amount_ml = Column('BLOOD_AMOUNT_ML', String)
    donor_id = Column('DONOR_ID', Integer)
    created_at = Column('CREATED_AT', Date, nullable=False, server_default=text('DEFAULT CURRENT_TIMESTAMP'))
    updated_at = Column('UPDATED_AT', Date, nullable=False, server_default=text('DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, transaction_type, blood_amount_ml, donor_id):
        self.transaction_type = transaction_type
        self.blood_amount_ml = blood_amount_ml
        self.donor_id = donor_id
