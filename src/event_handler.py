def  event_handler(event):
    event_cd = event.cd
    match (event_cd):
        case 'NDA':
            print('new donor')
        case _:
            print('Unknown code')