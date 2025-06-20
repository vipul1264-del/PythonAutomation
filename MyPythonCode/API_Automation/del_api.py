import requests

head = {
    "Accept": "text/plain",
    "Authorization": "bearer token"
}

response = requests.delete("https://fakerestapi.azurewebsites.net/api/v1/Activities/1", headers=head)

print(response.status_code)