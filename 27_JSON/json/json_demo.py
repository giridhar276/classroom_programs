#!/usr/bin/python

import json

# use loads method
# use loads if you want to parse
# from string buffer, otherwise use load method

with open('data.json') as f:
    data = f.read()
    jsondata = json.loads(data)

#print(jsondata)

for row in jsondata['rows']:
    print(row['title'],"-----",row['link'])
    
print("*******************************")

# or use load ( without s ) method
with open('data.json') as f:
    jsondata = json.load(f)

for row in jsondata['rows']:
    print(row['title'],"-----",row['link'])

    
