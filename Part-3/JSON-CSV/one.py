import json 
employees_json_csv='''
[
{"eid":101,"ename":"Rahul","avail":true,"loc":null},
{"eid":102,"ename":"Sonia","avail":false,"loc":null},
{"eid":103,"ename":"Priya","avail":true,"loc":null}
]
'''
print(type(employees_json_csv))
employees=json.loads(employees_json_csv)
print(type(employees))
print(employees)
