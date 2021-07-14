a=input().split(',')
d={}
b=[]
for x in a:
    l,r=map(int,x.split(':'))
    if l not in d:
        d[l]=r
    else:
        d[l]+=r
    b.append(l)
b.sort()

want=list(map(int,input().split(',')))
ans=[]

for x in want:
    flag=0
    for y in b:
        if y>=x and d[y]>0:
            d[y]-=1
            flag=1
            break
    if flag>0:
        ans.append('true')
    else:
        ans.append('false')

print(','.join(ans))