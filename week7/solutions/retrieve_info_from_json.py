import json

def retrieve_info_from_json(json_file_path, specific_key):
    with open(json_file_path, "r") as json_file:
        dict_json = json.load(json_file)
        return dict_json[specific_key]

print(retrieve_info_from_json("data_ex.json", "age"))
