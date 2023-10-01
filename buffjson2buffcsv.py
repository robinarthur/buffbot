import json
import pandas as pd

# open the json and read it into f-object and load it into data variable
with open('buff.json', 'r') as f:
    data = json.load(f)

list_of_urls = []

def pretty_print_json(d, indent=0):
    # print a dict easy human readable
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))
            

#pretty_print_json(data)

# iterate over the dict und store the urls in a list
for key, value in data.items():
    for url in value:
        list_of_urls.append(url)

# check the list for unique entries
print(len(list_of_urls))
print(len(set(list_of_urls)))
print(list_of_urls)

for url in list_of_urls:
    

