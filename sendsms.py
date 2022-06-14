from twilio.rest import Client
import random


def OTP():
    str1 = ''
    for i in range(6):
        str1 += str(random.randint(1, 9))
    return str1


sent_otp = OTP()


ACCOUNT_SID = 'AC121cc84bac166b7b54c52d8b16379f62'
AUTH_TOKEN = 'authtoken'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    from_='(845) 402-2616',
    to='+918882474233',
    body=sent_otp
)

print(message.sid)

while True:
    generated = input('enter otp sent')
    if sent_otp == generated:
        print('authenticated')
        break
