from .database.base import session
from .database.models import donor

def  event_handler(event):
    event_cd = event.cd
    if event_cd == 'NDA':
        _donor = event.donor
        model = donor.Donor(_donor.fname, _donor.lname, _donor.bloodType)
        session.add(model)
        session.commit()
        print('new donor')
    else:
        print('Unknown code')
    session.close()
