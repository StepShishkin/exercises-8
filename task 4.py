import json

json_lst = input()
python_lst = json.loads(json_lst)

print(sorted(python_lst, key=lambda x: x[1], reverse=True))