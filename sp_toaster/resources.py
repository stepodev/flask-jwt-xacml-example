# https://github.com/authzforce/restful-pdp/tree/develop/cxf-spring-boot-server/src/test/cli

from sp.models import XacmlRequest
import json, subprocess

from flask_restful import Resource
from flask_jwt_extended import (jwt_optional, get_jwt_identity)

import os
from PIL import Image


class ProtectedResource(Resource):
    @jwt_optional
    def post(self):

        if get_jwt_identity() is None:
            return {"message": "You needs JWT!"}, 401

        r = {}

        try:
            data = json.dumps(XacmlRequest.generate_request(subject=get_jwt_identity(),
                                                            resource="protected_toaster",
                                                            access_type="post"))

            # requests package causes pdp server to throw invalidargumentexception
            r = subprocess.check_output(["curl",
                                         '--header',
                                         'Content-Type: application/xacml+json',
                                         '--data',
                                         data,
                                         '-X',
                                         'POST',
                                         'http://localhost:10000/services/pdp'])

            r = r.decode('utf-8')

        except Exception as e:
            return {"message": "error!"}, 500

        if '"Response"' in r and '"Decision":"Permit"' not in r:
            return {"message": "not allowed!"}, 401

        if '"Decision":"Permit"' not in r:
            return {"message": "error!"}, 500

        try:
            image = Image.open(os.getcwd() + '/resources/toaster.JPG')
            image.show()
        except Exception as e:
            print(e)

        return {"message": "success"}
