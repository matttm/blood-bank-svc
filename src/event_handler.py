from .database.base import session
from .database.models import donor
from .enums import event_type
from .services.email_service.email_service import EmailService
import json

def  event_handler(event):
    print('event', event)
    print('body', (event['body']))
    body = json.loads(event['body'])
    print(body)
    event_cd = body.get("cd")
    if event_cd == event_type.NEW_DONOR_APPLICANT.code:
        _donor = body.get("donor")
        model = donor.Donor(_donor.get("fname"), _donor.get("lname"), _donor.get("bloodType"))
        session.add(model)
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
        session.commit()
    elif event_cd == event_type.DELETE_DONOR_APPLICANT.code:
        deletion = session.get(donor.Donor, body.get("donor").get("id"))
        session.delete(deletion)
        session.commit()
    else:
        print('Unknown code')
    EmailService().send_email('matttmaloney@gmail.com', None, None)
    session.close()
