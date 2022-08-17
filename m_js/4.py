import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

result = json.dumps(sampleJson, indent=4, separators=(",", " = "))
print(result)