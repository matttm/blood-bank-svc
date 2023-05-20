
class EventType():
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc

NEW_DONOR_APPLICANT = EventType("NDA", "New Donor Applicant")
EDIT_DONOR_APPLICANT = EventType("EDA", "Edit Donor Applicant")
DELETE_DONOR_APPLICANT = EventType("DDA", "Delete Donor Applicant")
NEW_TRANSACTION = EventType("NT", "New Transaction")
EDIT_TRANSACTION = EventType("ET", "Edit Transaction")

