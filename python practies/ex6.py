import pandas as pd

data = {
    'A' : [1,2,2,3,4,3,5],
    'B' : ['x','y','z','x','z','w','v']
}

df = pd.DataFrame(data)

remove_duplicate = df.drop_duplicates(keep='first') # compare row line by line
remove_duplicate_A = df.drop_duplicates(subset=['A'], keep=False)

print("clened (keep first)", remove_duplicate)
print("cleand (based on A)", remove_duplicate_A)

