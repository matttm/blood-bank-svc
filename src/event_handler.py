from database.base import session
from database.models import donor

def  event_handler(event):
    print(event)
    event_cd = event.get("cd")
    if event_cd == 'NDA':
        _donor = event.get("donor")
        model = donor.Donor(_donor.get("fname"), _donor.get("lname"), _donor.get("bloodType"))
        session.add(model)
        session.commit()
        print('new donor')
    else:
        print('Unknown code')
    session.close()
