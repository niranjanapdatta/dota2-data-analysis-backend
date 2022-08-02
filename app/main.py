import requests
import json


account_id = 108755293
res = requests.get(f'https://api.opendota.com/api/players/{account_id}')
print(json.dumps(json.loads(res.text), indent= 4))