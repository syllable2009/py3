import json

data = [ { 'a' : 4, 'b' : 5, 'c' : 6, 'd' : 7, 'e' : 8 } ]
json = json.dumps(data)
print(json)

import json
jsonData = '{"a":4,"b":5,"c":6,"d":7,"e":8}';

text = json.loads(jsonData)

print(text)