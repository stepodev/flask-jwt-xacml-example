from sp.models import XacmlRequest
import json
import requests

# r = XacmlRequest.generate_request(subject="stepo", resource="protected_green", access_type="post")
#
# data = json.dumps(XacmlRequest.generate_request(subject="stepo",
#                                                       resource="protected_red",
#                                                       access_type="post"))
#
# r = requests.post('http://127.0.0.1:10000/service/pdp',headers={"Content-Type": "application/xacml+json"},
#                     data=data)
#
#
# import os, subprocess
#
# print( subprocess.check_output(["curl",
#                                 '--header',
#                                 'Content-Type: application/xacml+json',
#                                 '--data',
#                                 data,
#                                 '-X',
#                                 'POST',
#                                 'http://localhost:10000/services/pdp']))

# r = '{"Response":[{"Decision":"Permit"}]}'
#
# if "Response" not in r and '"Decision":"Permit"' not in r:
#     print({"message": "not allowed!"}, 401 )
#
# if '"Decision":"Permit"' not in r:
#     print( {"message": "error!"}, 500)
#
from PIL import Image
import os

image = Image.open(os.getcwd() + '/resources/tv.jpeg')
image.show()