import requests

head = {
    "Accept": "text/plain",
    "Authorization": "bearer token(23b4kj25j34kjjkkj34)"
}

body = {
    "name" : "vipul",
    "profile": "software tester"
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json = body)

print(response.status_code)