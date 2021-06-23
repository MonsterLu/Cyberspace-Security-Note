class Solution():
    def buchongfu(self,x:list)->int:
        quan = len(x) - 1
        i = 0
        sum = 0
        while(i <= len(x) - 1):
            sum = sum + int(x[i]) * pow(10,quan)
            quan = quan - 1
            i = i + 1
        return sum

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
y = Solution()
c = y.buchongfu(u)
print(c)
