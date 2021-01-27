
import requests

def gen_otp(len):
    import math , random

    digits="0123456789"

    OTP=""

    for i in range(len):
        OTP += digits[math.floor(random.random() * 10  )]


    return OTP

def send_message(msisdn):
    otp = gen_otp(6)
    print (str(msisdn)[3:])
    print('OTP:' + str(otp))
    Api = 'http://173.212.218.174:6005/api/v2/SendSMS?SenderId=ZainSS&Is_Unicode=false&Is_Flash=false'
    message = 'To register USE OTP as '  + str(otp)
    Api = Api + '&Message=' + str(message)
    Api = Api + '&MobileNumbers=' + str(msisdn)[3:]
    Api = Api + '&ApiKey=TqEuq9o58233RcYkFIm5w1CS2HB7yJHejc0a3tbMpfg%3D&ClientId=94393ba7-afef-4744-880b-175368936e9b'


    r = requests.get(url=Api)
    # print(Api)
    print (r.status_code)
    return otp

