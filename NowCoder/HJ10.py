u = []
x = list(input(""))
last = len(x) - 1
i = 0
while(i < len(x)):
    if(x[last] == '0'):
        break
    if(x[last] not in u):
        u.append(x[last])
    last = last - 1
    i = i + 1
print(len(u))