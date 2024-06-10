l=[1,2,3,4,5]
count_1=3
for i in l:
    while count_1:
        k1=l[-1]
        l.pop()
        l.insert(0,k1)
        count_1-=1
print(l)

    