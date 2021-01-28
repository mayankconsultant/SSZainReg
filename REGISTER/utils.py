
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


    # r = requests.get(url=Api)
    # print(Api)
    # print (r.status_code)
    return otp


# from pytesseract import image_to_string
from PIL import Image , ImageFilter
import pytesseract
import os

import  re

def extract_text(filepath, id_num,first_name,last_name):
    img_grey = Image.open(filepath)
    img_grey = img_grey.convert('L')
    img_grey.save('media\ALL\grey_' + os.path.basename(filepath))
    img_grey = Image.open('media\ALL\grey_' + os.path.basename(filepath))
    blurImage = img_grey.filter(ImageFilter.DETAIL)
    os.remove('media\ALL\grey_' + os.path.basename(filepath))
    blurImage.save(r'media\ALL\blur_' + os.path.basename(filepath))
    config = ('-l eng --oem 1 --psm 3')

    try:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        k = pytesseract.image_to_string(Image.open(r'media\ALL\blur_' + os.path.basename(filepath)), config=config)
    except Exception as e:
        import cv2
        print('IN EXCEPTION CV2')
        # im = cv2.imread('./test3.jpg')
        k = pytesseract.image_to_string(cv2.imread(r'media\ALL\blur_' + os.path.basename(filepath)), config=config)




    # config = (' -l eng')

    # print (image_to_string(Image.open(filepath),lang='eng'))


    os.remove(r'media\ALL\blur_' + os.path.basename(filepath))
    points = 0
    if id_num in k :points +=1
    if first_name in k: points += 1
    if last_name in k: points += 1
    # print(k)
    # print( data in k)
    # print(k)
    # print(data in k)
    # k= k.split('\n')
    # for j in k:
    #     print( str(j) + ' Matched with ' + str(k))
    #     print(j in str(k))
    if points >=2 :
        return True
    else :
        return False
