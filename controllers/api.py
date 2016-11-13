import requests
import json

apiKey = '611b3ae684fcfa623a511f22aecba2f7'
payload = {
	"_id": "",
    "balance": "",
    "nickname": "",
    "rewards": "",
    "type": "Savings"
}
url = 'http://api.reimaginebanking.com/enterprise/accounts?key={}'.format(apiKey)
def get():
    response = requests.get(
        url,
	    params = payload,
	    headers={'content-type':'application/json'},
	)

return response