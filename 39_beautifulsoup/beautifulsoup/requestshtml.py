

import requests


urldata = requests.get("http://www.google.com")

print(urldata.text)
