import boto3
from botocore.exceptions import ClientError
from ..utility_service.utility_service import UtilityService

email_config = {
    'SENDER': None,
    # 'CONFIGURATION_SET': None,
    'EMAIL_AWS_REGION': None
}
class EmailService:
    singleton = None

    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def __init__(self) -> None:
        UtilityService.populate_config_from_environment(email_config)
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        self.SENDER = email_config['SENDER']

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        # self.RECIPIENT = email_config['RECIPIENT']

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the 
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        # self.CONFIGURATION_SET = email_config['CONFIGURATION_SET']

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        self.AWS_REGION = email_config['EMAIL_AWS_REGION']

        # Create a new SES resource and specify a region.
        self.client = boto3.client('ses',region_name=self.AWS_REGION)

    def send_email(self, recipient, code):
        template = __import__(f'${code}_template.py')
        # The subject line for the email.
        SUBJECT = template.SUBJECT

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = template.BODY_TEXT
                    
        # The HTML body of the email.
        BODY_HTML = template.BODY_HTML         

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = self.client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=self.SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=self.CONFIGURATION_SET,
            )
            # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])