#1,2,3,4,2
a=list(map(int,input().split(',')))
s=int(input())
n=len(a)
mx=-1
b=[0]*(n+1)
for i in range(n):
    b[i+1]=b[i]+a[i]
print(b)
for i in range(n):
    for j in range(i,n):
        if(b[j+1]-b[i]==s and mx<j-i+1):
            mx=j-i+1
print(mx)