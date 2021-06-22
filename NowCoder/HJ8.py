class Solution():
    def shengxu(inputs:dict)->dict:
        print(inputs)

        return inputs
x = {}
count = int(input(""))
while(count != 0):
    keyin = input("")
    keyin1 = keyin.split()
    if(len(keyin1) == 1):
        x[int(keyin1[0])] = 0
    elif(int(keyin1[0]) in x):
        x[int(keyin1[0])] = int(keyin1[1]) + x[int(keyin1[0])]
    else:
        x[int(keyin1[0])] = int(keyin1[1])
    count = count - 1

y = Solution()
x1 = y.shengxu(x)
for i in x1:
    print(i , x1[i])
