from twilio.rest import Client

from datetime import datetime

class sms:
    def msg(self,prediction):
        account_sid = 'AC9064b095ee5db08a3045efe80140b72e'
        auth_token = '880c31974f1e34fe3726ab1f2db3f802'
        client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #   messaging_service_sid='MG75dfa40854e9bbb803e81503795cb3f6',
        #   body='//website',
        #   to='+918547751321'
        # )
        # print(message.sid)

        numbers = ['+918547751321','+919746458177','+918137019259']

        # prediction = 1

        if prediction==1:
            print("SMS sending")
            for number in numbers:
                message = client.messages.create(
                messaging_service_sid='MG520b43f804e8aa31430192f7036e9edb',
                body='Disaster predicted\nwebsite: https://abhiramanish.github.io/disaster/\n'+str(datetime.now()),
                to=number
                )
                print(message.sid)


# obj = sms()
# obj.msg(1)