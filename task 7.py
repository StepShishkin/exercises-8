import json

def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(json.dumps(result))
    return wrapper

@to_json
def info():
    return {"Moscow": 1, "Novosibirsk": 2, "Los Angeles": 3}

@to_json
def calculate(a, b):
    return a + b

info()
calculate(5, 3)
