

# JSON SCHEMA SNIFFER

The JSON sniffer is a python tool used to sniff the schema of a JSON file and dump it in a folder within the project.

# Dependency
python 3x

# Usage
To execute the program, navigate into the projects main directory and run the following command.

```bash
python3 main.py <name(s) of json file(s)>
```

Alternatively you can add the file(s) you want to get schema for as part of command arguments seperated by space

```bash
python3 main.py <name of file 1> <name of file2>
```

For this JSON files in this repository, run

```bash
python3 main.py data_1.json data_2.json
```

# Test

To execute the test, run the following command

```bash
python3 -m unittest tests.test
```
