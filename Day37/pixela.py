import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER = "plam7"
TOKEN = "fxq5guyvvbh"

user_params = {
    "token":TOKEN, 
    "username":USER, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes", 
    "thanksCode":"ThisIsThanksCode"
}

# response = requests.post(url=pixela_endpoint, json=user_params, timeout=10)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_params = {
    "id":"graph001",
    "name":"coding-days",
    "unit":"commit",
    "type":"int",
    "color":"sora",
    "timezone":"Europe/Sofia",
    "isSecret":False,
    "publishOptionalData":True
}

headers = {"X-USER-TOKEN":TOKEN}

response = requests.post(url=graph_endpoint, 
                         json=graph_params, 
                         headers=headers, 
                         timeout=10)

print(response.text)