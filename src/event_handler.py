from .database.base import session
from .database.models import donor, transaction
from .enums import event_type
from .services.email_service.email_service import EmailService
import json

def  event_handler(event):
    print('event', event)
    print('body', (event['body']))
    donorId = None
    email = None
    body = json.loads(event['body'])
    print(body)
    event_cd = body.get("cd")
    if event_cd == event_type.NEW_DONOR_APPLICANT.code:
        _donor = body.get("donor")
        model = donor.Donor(_donor.get("fname"), _donor.get("lname"), _donor.get("bloodType"))
        session.add(model)
        donorId = model.donor_id
        session.commit()
        print('new donor')
    elif event_cd == event_type.EDIT_DONOR_APPLICANT.code:
        _donor = body.get("donor")
        session.query(donor.Donor). \
            filter(donor.Donor.donor_id == _donor.get("id")). \
                update({
                    "first_name": _donor.get("fname"),
                    "last_name": _donor.get("lname"),
                    "blood_type": _donor.get("bloodType")
                })
        donorId = _donor.get("id")
        session.commit()
    elif event_cd == event_type.DELETE_DONOR_APPLICANT.code:
        deletion = session.get(donor.Donor, body.get("donor").get("id"))
        session.delete(deletion)
        donorId = body.get("donor").get("id")
        session.commit()
    elif event_cd == event_type.NEW_TRANSACTION.code:
        _transaction = body.get("transaction")
        model = transaction.Transaction(
            _transaction.get("transactionType"),
            _transaction.get("bloodAmountML"),
            _transaction.get("donorId")
        )
        session.add(model)
        donorId = model.donor_id
        session.commit()
    elif event_cd == event_type.EDIT_TRANSACTION.code:
        _transaction = body.get("transaction")
        session.query(donor.Donor). \
            filter(transaction.Transaction.transaction_id == _transaction.get("transactionIfd")). \
                update({
            _transaction.get("transactionType"),
            _transaction.get("bloodAmountML"),
            _transaction.get("donorId")
                })
        donorId = _transaction.get("donorId")
        session.commit()
    else:
        print('Unknown code')
    if donorId != None:
        _donor = session.get(donor.Donor, donorId)
        email = _donor.email if _donor != None else None
    if email != None:
        EmailService().send_email(email, event_cd)
    session.close()
