from .database.base import session
from .database.models import donor

def  event_handler(event):
    print(event)
    body = event['body']
    print(body)
    event_cd = body.get("cd")
    if event_cd == 'NDA':
        _donor = body.get("donor")
        model = donor.Donor(_donor.get("fname"), _donor.get("lname"), _donor.get("bloodType"))
        session.add(model)
        session.commit()
        print('new donor')
    else:
        print('Unknown code')
    session.close()
