import requests,json,qrcode,time
from PIL import Image

def Bili_Login() :
    response = requests.get("http://passport.bilibili.com/qrcode/getLoginUrl").json()
    response = response['data']
    oauthKey = response['oauthKey']
    print(oauthKey)
    img = qrcode.make(response['url'])
    img.save('test.png')
    img.show()
    response = requests.post("http://passport.bilibili.com/qrcode/getLoginInfo",data = {'oauthKey':oauthKey}).json()
    #print(response['data'])
    response = requests.post("http://passport.bilibili.com/qrcode/getLoginInfo",data = {'oauthKey':oauthKey})
    DataJson = response.json()
    while DataJson['data'] == -4 or DataJson['data'] == -5:
        time.sleep(1)
        response = requests.post("http://passport.bilibili.com/qrcode/getLoginInfo",data = {'oauthKey':oauthKey})
        DataJson = response.json()
        print("waiting for a scan...")


    while DataJson['data'] == -1:
        #密钥错误
        print("an error occured...program gonna exit...")


    while DataJson['data'] == -2:
        #密钥超时
        print("time out...")
        return -2
        break

    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    return cookies
    

Bili_Login()