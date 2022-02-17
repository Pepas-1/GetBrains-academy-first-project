import requests

req=requests.get(input('Input the URL:\n'))
if req:
    req=req.json()
    print(req["content"])
else:
    print('Invalid quote resource!')