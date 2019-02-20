filename = r'Chapter 10\10.2 c.py\learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line)
    line = line.replace('Python','c')
    print(line)