'''
consume Rest API and write users data into new json file
API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fields:None
Access Type:Public
'''
import requests
import json 

fp=open('users.json','w')
users_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_resp.json()

#dump python data into json file
json.dump(users,fp)
print("New JSON created successfully")
fp.close()
