import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":"fxq5guyvvbh", 
    "username":"plam7", 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes", 
    "thanksCode":"ThisIsThanksCode"
}

response = requests.post(url=pixela_endpoint, json=user_params, timeout=10)

print(response.status_code)