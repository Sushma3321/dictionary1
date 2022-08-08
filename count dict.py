dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for keys in dict1.values():
    for i in keys:
        c=c+1

print(c)
    
    
