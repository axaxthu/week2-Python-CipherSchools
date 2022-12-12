print(list(map(lambda x:x**2,range(5))))

a=[]
for i in range(5) :
    temp=[]
    for j in range (5):
        temp.append(j)
    a.append(temp)   
print(a)

print([i for i in range(5)])
#
n=5
print([[max(i+1,j+1,n-1,n-j)for j in range(n)]for i in range(n)])