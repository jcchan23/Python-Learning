with open(r'Chapter 10\10.1 python.py\learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print('\n')

filename = r'Chapter 10\10.1 python.py\learning_python.txt'
with open(filename) as file_object2:
    for line in file_object2:
        print(line.rstrip())
print("\n")

with open(filename) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.rstrip())