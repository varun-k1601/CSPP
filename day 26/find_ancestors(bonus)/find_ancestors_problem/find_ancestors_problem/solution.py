import json

# Input string
input_str = '{"value": 1, "children": [{"value": 2, "children": []}, {"value": 3, "children": [{"value": 4, "children": []}]}]} 4 2'

# Split the input into JSON part and values
parts = input_str.rsplit(" ", 2)  # Split from the right to separate the last two values

# Parse the JSON part
json_obj = json.loads(parts[0])

# Convert the other two values into integers
value1 = int(parts[1])
value2 = int(parts[2])

# Print the results
print("JSON object:", json_obj)
print("Value 1:", value1)
print("Value 2:", value2)
# {"value": 1, "children": [{"value": 2, "children": []}, {"value": 3, "children": [{"value": 4, "children": []}]}]} 4 2