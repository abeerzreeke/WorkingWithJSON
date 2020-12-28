import json

sampleJson = """{ 
    "company":{
        "employee":{
            "name":"emma",
            "payable":{
                "salary":7000,
                "bonus":800
            }
        }
    }
}"""


data = json.loads(sampleJson)
#Access the nested key “salary” from the above JSON-string
print(data["company"]["employee"]["payable"]["salary"])

#Sort the dictionary key-value pairs inside “payable” alphabetically, by their key, using code 
# Save the dictionary as JSON to a file
with open("data_file.json", "w") as file_obj:
    json.dump(data, file_obj, indent = 2, sort_keys=True)

