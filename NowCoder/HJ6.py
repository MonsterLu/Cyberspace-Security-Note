class Solution:
    def zhishu(inputs: int)->list :
        res = []
        i = 2
        x = inputs
        while(x != 1):
            if(x % i == 0):
                res.append(i)
                x = x // i
                u = x % 10
                if(u == 1 or u == 7):
                    if(u != 0 and x % u != 0 ):
                        res.append(x)
                        break
            else:
                i = i + 1
        return res
#x = input("enter:")
#x1 = int(x)
x1 = 93938
y = Solution
u = y.zhishu(x1)
for i in u:
    print(i,end = ' ')
#print(y.zhishu(x))
