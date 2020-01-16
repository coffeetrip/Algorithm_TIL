import os
import sys
import urllib.request
client_id = "n31k7m35mw"
client_secret = "chXSuXiT7WitLV51HcgUihRYDYHGYyXDyC5KsTEq"
encText = urllib.parse.quote("천안시")
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    mystr = response_body.decode('utf-8')
    # false, true를 대문자로 replace를 해주고,
    mystr = mystr.replace('true',"True")
    mystr = mystr.replace('false',"False")
    
    # string -> json 타입으로 바꾸자
    mydic = eval(mystr)
    
    # 차례대로 끼워맞추다 보면 아래의 값으로 출력 할 수 있다.
    print(mydic['result']['items'][0]['point']['y'])
    print(mydic['result']['items'][0]['point']['x'])
else:
    print("Error Code:" + rescode)

