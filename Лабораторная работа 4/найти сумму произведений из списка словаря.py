
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    i= sum(item ["score"]*item["weight"] for item in data)
    a= round (i, 3)
    return a
print(task())


