filepath = 'Chapter 10/10.10 words.py/text.txt'

try:
    with open(filepath) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file does not exist."
    print(msg)
else:
    print(contents.lower().count('the'))