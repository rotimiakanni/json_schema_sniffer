import json
import os, sys
from unicodedata import name

def sniff_json_schema(json_data: dict, schema: dict) -> dict:
    """
    Sniffs the schema of a JSON data recursively.

    args: 
        -json_data: a dictionary containing the JSON data
        -schema: a dictionary where the schema is added

    returns:
        dict: a dictionary containing the schema of the JSON data

    """
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == 'attributes':
                continue  
            if isinstance(value, dict):
                schema[key] = {
                    "type": "object",
                    "properties": {}
                }
                sniff_json_schema(value, schema[key]["properties"]) # recursive call for object properties
            elif isinstance(value, list) and len(value) > 0:
                if isinstance(value[0], dict):
                    schema[key] = {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    }
                    sniff_json_schema(value[0], schema[key]["items"]["properties"]) # recursive call for array properties
                elif isinstance(value[0], str):
                    schema[key] = {
                        "type": "enum",
                        "items": {
                            "type": "string",
                            "enum": value
                        }
                    }
            elif isinstance(value, list) and len(value) == 0:
                schema[key] = {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": value
                    }
                }
            elif isinstance(value, str):
                schema[key] = {
                    "type": "string"
                }
            elif isinstance(value, bool):
                schema[key] = {
                    "type": "boolean"
                }
            elif isinstance(value, int):
                schema[key] = {
                    "type": "integer"
                }
            schema[key]["description"] = f"{key} is of type {schema[key]['type']}"
            schema[key]["tag"] = f"Tag for {key}"
            schema[key]["required"] = False
    elif isinstance(json_data, list) and len(json_data) > 0:
        if isinstance(json_data[0], dict):
            schema["items"] = {
                "type": "array",
                "properties": {}
            }
            sniff_json_schema(json_data[0], schema["items"]["properties"])
        else:
            schema["items"] = {
                "type": "enum",
                "enum": json_data
            }

def dump_json_schema(json_file_path:str, schema_dir:str):
    """
    Reads a JSON file, sniffs its schema, and dumps the output to a 
    file in the ./schema directory.
    """
    try:
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
            schema = {}
            sniff_json_schema(json_data['message'], schema)

        output_file_path = os.path.join(schema_dir, f"schema_{os.path.splitext(os.path.basename(json_file_path))[0].split('_')[-1]}.json")
        with open(output_file_path, 'w') as output_file:
            json.dump(schema, output_file, indent=4)
    except FileNotFoundError:
        print(f"{json_file_path.split('/')[-1]} file not found in './data/'")
