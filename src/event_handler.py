from database.base import session
from database.models import donor

def  event_handler(event):
    event_cd = event.cd
    match (event_cd):
        case 'NDA':
            _donor = event.donor
            model = donor.Donor(_donor.fname, _donor.lname, _donor.bloodType)
            session.add(model)
            session.commit()
            print('new donor')
        case _:
            print('Unknown code')
    session.close()
