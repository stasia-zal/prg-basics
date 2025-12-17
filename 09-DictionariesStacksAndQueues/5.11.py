import json

try:
    # Try to read existing file
    with open('voting.json', 'r', encoding='utf-8') as file:
        voting = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    # File does not exist → create empty voting
    voting = {}

# Read the contents of the json file


# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in voting:
    voting[person_name]+=1
else:
    voting[person_name]=1

# Save voting data to json file
with open('voting.json','w',encoding='utf-8') as file:
    json.dump(voting,file)