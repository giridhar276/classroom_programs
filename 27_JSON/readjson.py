import json
json_data = open("colors.json")
data = json.load(json_data)
print(list((data.keys())))
