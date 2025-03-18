import os
from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class sms:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.messaging_service_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
        self.client = Client(self.account_sid, self.auth_token)
        self.numbers = ['+918547751321', '+919746458177', '+918137019259']

    def send_msg(self, prediction):
        if prediction == 1:
            print("SMS sending...")
            for number in self.numbers:
                try:
                    message = self.client.messages.create(
                        messaging_service_sid=self.messaging_service_sid,
                        body=f'Disaster predicted\nWebsite: https://abhiramanish.github.io/disaster/\n{datetime.now()}',
                        to=number
                    )
                    print(f"Message sent to {number}: {message.sid}")
                except Exception as e:
                    print(f"Failed to send message to {number}: {str(e)}")

# Usage Example
# obj = SMS()
# obj.send_msg(1)
