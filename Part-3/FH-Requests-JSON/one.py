import requests
rest_api_url='https://jsonplaceholder.typicode.com/users'
user_resp=requests.get(rest_api_url)
status_code=user_resp.status_code
print(status_code)

users=user_resp.json()
print(users)