import requests
import json
login_url = "https://os.ncuos.com/api/user/token"
return_url = "https://os.ncuos.com/api/user/profile/basic"
session = requests.session()

login_page = session.get(login_url)
p = login_page.text.find('VerificationToken')+len('VerificationToken')+4
token = login_page.text[p:login_page.text.find("'", p)]

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'VerificationToken': token
       }
session.headers.update(headers)

data = {
    'username': "7702118043",
    'password': "456654",
    'remember': True
    }

response1 = session.post(login_url, data=json.dumps(data))
print(response1.text)


