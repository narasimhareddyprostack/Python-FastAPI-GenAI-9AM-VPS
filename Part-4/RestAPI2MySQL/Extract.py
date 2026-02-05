import requests

rest_api_url='https://jsonplaceholder.typicode.com/users'
user_resp=requests.get(rest_api_url)
print(user_resp.status_code)
users=user_resp.json()
print(type(users))
print(len(users))