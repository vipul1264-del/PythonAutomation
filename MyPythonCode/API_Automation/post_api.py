import requests

header = {
    "Accept": "text/plain",
    "content-Typer" : "application/json"
}

body = {
    "name" : "Vipul",
    "profile" : "Tester",
    "status" : "Active"
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", 
                         headers=header, json = body)

print(response.status_code)