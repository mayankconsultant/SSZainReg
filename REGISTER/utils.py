from twilio.rest import Client

from django.conf import settings

def gen_otp(len):
    import math , random

    digits="0123456789"

    OTP=""

    for i in range(len):
        OTP += digits[math.floor(random.random() * 10  )]

    return OTP

def send_sms(msisdn):
    otp = gen_otp(6)
    print(otp)
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.ACCOUNT_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="To register USE OTP as " + str (otp) ,
        from_='+12015968801', #settings.FROM_PHONE,
        to='+917718035086' # + str(msisdn)
    )

    print(message.sid)


    # account_sid = 'AC0bc30ff886a6f08d90527c18adea426a'
    # auth_token = 'c6f7cbb0ca6904aea996be3162223bc1'
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body='Hello! Your OTP for Registration is ' + str(otp),
    #     to='whatsapp:+917718035086'
    # )
    #
    # print(message.sid)

    return otp