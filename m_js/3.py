import json
from unittest import result

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

result = json.dumps(sampleJson, indent=2, separators=(",", " = "))

print(result)
