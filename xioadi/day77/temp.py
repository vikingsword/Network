import base64

import requests

# res = requests.get('http://demo.vikingsword.top:1234/xui/inbounds')
# print(res.content)

str = 'glassfish && port=\"4848\"'
r = base64.b64encode(str.encode('utf-8'))
print(r)
rs = base64.b64decode(r)
print(rs)