x= {'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}

z={}
for i in x:
    for i,j in y.items():
        if x[i]==j:
            z[i]=j
print(z)