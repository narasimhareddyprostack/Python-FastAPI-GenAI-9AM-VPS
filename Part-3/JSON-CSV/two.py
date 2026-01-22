import json 
employees=[
    {'eid': 101, 'ename': 'Rahul', 'avail': True, 'loc': None}, 
    {'eid': 102, 'ename': 'Sonia', 'avail': False, 'loc': None},
    {'eid': 103, 'ename': 'Priya', 'avail': True, 'loc': None}
]
employees_json_str=json.dumps(employees)
print(employees_json_str)