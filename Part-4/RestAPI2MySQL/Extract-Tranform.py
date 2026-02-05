import requests
#Extract
rest_api_url='https://jsonplaceholder.typicode.com/users'
user_resp=requests.get(rest_api_url)
print(user_resp.status_code)
users=user_resp.json()
print(type(users))
print(len(users))
#Tranform
user_data=[]
for user in users:
    id=user['id']
    name=user['name']
    company=user['company']['name']
    user_data.append((id,name,company))

print(len(user_data))
print(user_data)