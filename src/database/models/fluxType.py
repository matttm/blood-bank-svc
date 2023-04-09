
from sqlalchemy import Column, String

from base import Base


class TransactionType(Base):
    __tablename__ = 'TRANSACTION_TYPE'

    transaction_type_id = Column('TRANSACTION_TYPE_ID', String, primary_key=True)
    transaction_type_desc = Column('TRANSACTION_TYPE_DESC', String)

    def __init__(self, transaction_type_id, transaction_type_desc):
        self.transaction_type_id = transaction_type_id
        self.transaction_type_desc = transaction_type_desc
