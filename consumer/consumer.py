import requests, subprocess, json, base64
from sp.models import XacmlRequest

# start: ~/workspace/homeauto/vortrag/pdp$ ./authzforce-ce-restful-pdp-cxf-spring-boot-server-1.3.0.jar
requests.delete("http://127.0.0.1:3000/users")

# versuchen wir mal ein rotes fenster aufzumachen
r = requests.post('http://127.0.0.1:4000/protected_toaster')

print("protected_toaster antwort:\n", r, "\n", r.text)

# wir brauchen also einen json web token. lass einloggen!
r = requests.post('http://127.0.0.1:3000/login', data={"username": "stepo", "password": "stepo "})

print("login antwort:\n", r, "\n", r.text)

# okay, dann erst registrieren
r = requests.post('http://127.0.0.1:3000/registration', data={"username": "stepo", "password": "stepo "})

print("registration antwort:\n", r, "\n", r.text)

access_token = json.loads(r.text)["access_token"]
refresh_token = json.loads(r.text)["refresh_token"]

# was stehtn da drin?
print("header:", base64.b64decode(access_token.split('.')[0]))
print("payload:", base64.b64decode(access_token.split('.')[1] + "=="))

# jetzt haben wir einen jwt. lass nochmal versuchen!

r = requests.post('http://127.0.0.1:4000/protected_toaster', headers={"authorization": "Bearer " + access_token})

print("protected_toaster antwort:\n", r, "\n", r.text)

# bei nem anderen service?
r = requests.post('http://127.0.0.1:5000/protected_tv', headers={"authorization": "Bearer " + access_token})

print("protected_tv antwort:\n", r, "\n", r.text)

# darf denn jeder an die resource ran?
r = requests.post('http://127.0.0.1:3000/registration', data={"username": "jpr", "password": "jpr "})
access_token = json.loads(r.text)["access_token"]

r = requests.post('http://127.0.0.1:4000/protected_toaster', headers={"authorization": "Bearer " + access_token})

print("protected_toaster antwort:\n", r, "\n", r.text)

# wie entscheidet denn die resource wer darf? XACML!
data = json.dumps(XacmlRequest.generate_request(subject="stepo",
                                                resource="protected_toaster",
                                                access_type="post"), indent=2)
# ./Request.json

r = subprocess.check_output(["curl",
                             '--header',
                             'Content-Type: application/xacml+json',
                             '--data',
                             data,
                             '-X',
                             'POST',
                             'http://localhost:10000/services/pdp'])

r = r.decode('utf-8')
print(r)