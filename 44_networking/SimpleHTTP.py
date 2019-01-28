
import http.client

h = http.client.HTTPConnection("www.google.com")
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)
text = data.readlines()

# t is in the bytes.. so we need to convert into utf-8 format
for t in text:
    print(t.decode('utf-8'))

