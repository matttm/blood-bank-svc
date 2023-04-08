from .database.base import session
from .database.models import donor
import json

def  event_handler(event):
    print('event', event)
    print('body', (event['body']))
    body = json.loads(event['body'])
    print(body)
    event_cd = body.get("cd")
    if event_cd == 'NDA':
        _donor = body.get("donor")
        model = donor.Donor(_donor.get("fname"), _donor.get("lname"), _donor.get("bloodType"))
        session.add(model)
        session.commit()
        print('new donor')
    elif event_cd == 'EDA':
        _donor = body.get("donor")
        edit = session.get(donor.Donor, body.get("id"))
        edit.firstName = _donor.get("fname")
        edit.lastName = _donor.get("lname")
        edit.bloodType = _donor.get("bloodType")
        session.commit()
    elif event_cd == 'DD':
        deletion = session.get(donor.Donor, body.get("id"))
        session.delete(deletion)
        session.commit()
    else:
        print('Unknown code')
    session.close()
