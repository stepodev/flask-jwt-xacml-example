import json

class XacmlRequest():
    data = json.loads("""
{"Request":{"ReturnPolicyIdList":false,"CombinedDecision":false,"Category":[
  {"CategoryId":"urn:oasis:names:tc:xacml:1.0:subject-category:access-subject","Attribute":[{"IncludeInResult":false,"AttributeId":"urn:oasis:names:tc:xacml:1.0:subject:subject-id","DataType":"http://www.w3.org/2001/XMLSchema#string","Value":[
      "subject"
    ]}]}
  ,{"CategoryId":"urn:oasis:names:tc:xacml:3.0:attribute-category:resource","Attribute":[{"IncludeInResult":false,"AttributeId":"urn:oasis:names:tc:xacml:1.0:resource:resource-id","DataType":"http://www.w3.org/2001/XMLSchema#anyURI","Value":[
      "resource"
    ]}]}
  ,{"CategoryId":"urn:oasis:names:tc:xacml:3.0:attribute-category:action","Attribute":[{"IncludeInResult":false,"AttributeId":"urn:oasis:names:tc:xacml:1.0:action:action-id","DataType":"http://www.w3.org/2001/XMLSchema#string","Value":[
      "access_type"
    ]}]}
  ,{"CategoryId":"urn:oasis:names:tc:xacml:3.0:attribute-category:environment","Attribute":[]}
]}}
""")

    @classmethod
    def generate_request(cls, subject, resource, access_type):

        request = cls.data
        for i in range(0, len(request["Request"]["Category"])):
            if request["Request"]["Category"][i]["CategoryId"] == "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject":
                request["Request"]["Category"][i]["Attribute"][0]["Value"][0] = subject

            if request["Request"]["Category"][i]["CategoryId"] == "urn:oasis:names:tc:xacml:3.0:attribute-category:resource":
                request["Request"]["Category"][i]["Attribute"][0]["Value"][0] = resource

            if request["Request"]["Category"][i]["CategoryId"] == "urn:oasis:names:tc:xacml:3.0:attribute-category:action":
                request["Request"]["Category"][i]["Attribute"][0]["Value"][0] = access_type

        return request
