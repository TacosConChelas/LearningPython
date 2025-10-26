# https://www.apple.com/itunes/search?entity=son&limit=1&term=
import sys
import requests
import urllib

import json

if len(sys.argv) != 2:
    sys.exit()

termino = urllib.parse.quote_plus(sys.argv[1])

response = requests.get(f"https://itunes.apple.com/search?term={termino}&entity=musicTrack&limit=5", timeout=10)

response.raise_for_status()

# datos = response.json()
# pretty_json = json.dumps(datos, indent=2, ensure_ascii=False)
# print(pretty_json)

objeto = response.json()
for results in objeto["results"]:
    print(results["trackName"])


