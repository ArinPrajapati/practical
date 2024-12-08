import json

# Write a program to read and write data in JSON format using the json module.
# Data to be written to JSON
data = {"name": "John", "age": 30, "city": "New York"}

# Writing JSON data to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON data from a file
with open("data.json", "r") as json_file:
    data_loaded = json.load(json_file)

print(data_loaded)
