import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

result = json.loads(sampleJson)
print(result["company"]["employee"]["payble"]["salary"])