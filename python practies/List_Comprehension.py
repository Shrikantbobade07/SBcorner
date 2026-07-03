
amounts= [100,-20,300,-25,500]
# using regular list
for i in amounts:
     if i>0:
          print (i)

# using list comprehencis
positive = [x for x in amounts if x > 0]
print(positive)