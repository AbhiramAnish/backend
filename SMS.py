import os
from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SMS:
    def __init__(self):
        self.account_sid = "AC93ad21169738fa74300621392c97a4ab"
        self.auth_token = "c7d4050d6acbd0bebc1156510365f100"
        self.messaging_service_sid = "MG75dfa40854e9bbb803e81503795cb3f6"
        self.client = Client(self.account_sid, self.auth_token)
        self.numbers = ['+918547751321', '+919746458177', '+918137019259', '+917736458528']
        # self.numbers = ['+918547751321']

    def send_msg(self, disaster):
        if disaster == 0:       # if flood, english msg
            self.body = ("Possibilty of Flood in your area, please move to a safe location\n"
                         "Website: https://abhiramanish.github.io/disaster/ \n"
                         f"{datetime.now()}")
        elif disaster == 1:     # if landslide, english msg
            self.body = ("Possibilty of Landslide in your area, please move to a safe location\n"
                         "Website: https://abhiramanish.github.io/disaster/ \n"
                         f"{datetime.now()}")
        elif disaster == 2:     # if flood, malayalam msg
            self.body = ("നിങ്ങളുടെ പ്രദേശം വെള്ളപ്പൊക്ക ഭീഷണിയിലാണ്, എത്രയും പെട്ടെന്ന് സുരക്ഷിതമായ സ്ഥലത്തേക്ക് മാറുക.\n"
                         "Website: https://abhiramanish.github.io/disaster/ \n"
                         f"{datetime.now()}")
        elif disaster == 3:     # if landslide, malayalam msg
            self.body = ("നിങ്ങളുടെ പ്രദേശം ഉരുൾപ്പൊട്ടൽ ഭീഷണിയിലാണ്, എത്രയും പെട്ടെന്ന് സുരക്ഷിതമായ സ്ഥലത്തേക്ക് മാറുക.\n"
                         "Website: https://abhiramanish.github.io/disaster/ \n"
                         f"{datetime.now()}")
        print("SMS sending...")
        for number in self.numbers:
            try:
                message = self.client.messages.create(
                    messaging_service_sid=self.messaging_service_sid,
                    body=self.body,
                    to=number
                )
                print(f"Message sent to {number}: {message.sid}")
            except Exception as e:
                print(f"Failed to send message to {number}: {str(e)}")

if __name__ == "__main__":
    # Usage Example
    obj = SMS()
    obj.send_msg(3)