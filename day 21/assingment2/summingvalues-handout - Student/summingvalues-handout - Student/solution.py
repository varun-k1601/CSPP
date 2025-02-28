def sum_values(dictionary):
    #start your code here
    pass

def display_sum(dictionary):
    #start your code here
    total=0
    for key,values in dictionary.items():
        total+=values
    print(f"Sum: {total}")
def read_input():
    
    input_str = input().strip()
    
    if input_str == 'values = {}':
        return {}
    input_str = input_str.strip('{}')
    pairs = input_str.split(', ')
    dictionary = {}
    for pair in pairs:
        
        key, value = pair.split(': ')
        key = key.strip('"')
        value = int(value.strip('"'))
        dictionary[key] = value
    
    return dictionary


dictionary = read_input()

display_sum(dictionary)


