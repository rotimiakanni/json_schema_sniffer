import sys
from sniff_json import dump_json_schema


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for file_name in sys.argv[1:]:
            json_file_path = './data/' + file_name  # Path to the JSON file
            schema_dir = './schema/'  # Directory to dump the schema
            dump_json_schema(json_file_path, schema_dir)
    else:
        for file_name in ['data_1.json', 'data_2.json']:
            json_file_path = './data/' + file_name  # Path to the JSON file
            schema_dir = './schema/'  # Directory to dump the schema
            dump_json_schema(json_file_path, schema_dir)