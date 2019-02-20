import json
filepath = r'Chapter 10\10.11 favorite_number.py\favorite_number.txt'

with open(filepath,'r') as file_object:
    contents = json.load(file_object)
print("I know your favourite number! It's " + str(contents))