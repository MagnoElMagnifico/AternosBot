import json

# Reads the content on a json file given its path
def read(dir_name : str):
  json_file = open(dir_name)
  data = json.loads("".join(json_file.readlines()))
  json_file.close()
  return data

# Writes the dict given (data) in a json file already created
def write(dir_name : str, data : dict):
  json_file = open(dir_name, "w")
  json_file.write(json.dumps(data, indent=2))
  json_file.close()
