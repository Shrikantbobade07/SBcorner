'''if[]:
    print("yes")
else:
    print("No")
    '''


'''data = [[1,2],[3,4]]
for x, y in data:
    print (x + y, end = ' ')'''

'''def f (x,y=2):
    return x+y
print(f (3, None)) # you got error or '''

def f(x, y=2):
    if y is None:
        y=2
    return x+y
print (f(3, None))
