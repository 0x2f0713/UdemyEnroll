import requests
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import codecs

def getInfinityFreeCookie(): 
    getRawData_request = requests.post("https://mess.0x2f0713.cf/api/enroll_udemy/logs",verify=False)
    x = re.findall("[a-f0-9]{32}", getRawData_request.text)
    for index_x,i in enumerate(x):
        x[index_x] = codecs.decode(i,"hex")
    iv = x[1]
    ct = x[2]
    cipher = AES.new(x[0], AES.MODE_CBC, iv)
    res = cipher.decrypt(ct).hex()
    print(res)
    return res

getInfinityFreeCookie()