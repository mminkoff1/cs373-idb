import requests
import json 


resp = requests.get("https://api.github.com/repos/mminkoff1/cs373-idb/contributors")

print (resp.status_code)

data = json.loads(resp.text)


for i in range(len(data)):
	print "Login: " + str(data[i]["login"]) + " Commits: " + str(data[i]["contributions"])