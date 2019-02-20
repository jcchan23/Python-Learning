import json
filepath = r'Chapter 10\10.11 favorite_number.py\favorite_number.txt'

number = input("please input your favorite number: ")

with open(filepath,'a') as file_object:
    json.dump(number,file_object)
