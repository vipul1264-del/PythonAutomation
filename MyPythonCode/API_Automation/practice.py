import requests

head = {
    "Accept" : "text"
}

data = {
    "name" : "anusha",
    "company" : "sun mobility"
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5", headers=head)

print(f"this is from get method ::{response.status_code}")

print(response.json())


response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=data)

print(f"from post method ::{response.status_code}")

response = requests.delete("https://fakerestapi.azurewebsites.net/api/v1/Activities/2", headers= head)

print(f"this is from delete method ::{response.status_code}")