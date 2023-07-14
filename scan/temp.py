import base64
import os

with open('temp.txt', 'rb') as f:
    res = f.read()
    res_encode = base64.b64encode(res)
    print(res_encode)
