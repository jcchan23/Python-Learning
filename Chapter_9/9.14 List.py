from collections import OrderedDict
Words = OrderedDict()
Words['int']='Integer number'
Words['float']='float number'
Words['double']='double float number'
Words['char']='character word'
Words['class']='a kind of set and function'
Words['list']='a kind of variable table in python'
Words['tuple']='a kind of fixed table in python '
Words['while']='a kind of keywords in loop'
Words['for']='another kind of keywords in loop'
Words['if']=' a kind of keywords in condition'

for name,value in Words.items():
    print(name + ": " + value + "\n")
