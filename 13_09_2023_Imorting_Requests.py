from requests import get
from datetime import datetime

def send_request():
    # taking api respone from the url 
    print(get("http://httpbin.org"))

    # Json Response of URL Api
    res = get("http://httpbin.org/json")
    print(res.json())

    #Getting Status code of Json respone
    print("Status Code: " + str(res.status_code) + " Respone Time: " + str(datetime.now()))

# calling send_request
send_request()