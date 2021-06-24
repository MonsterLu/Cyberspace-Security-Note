#明明的随机数
class Solution():
    def quchong_paixu(self,inputs:list)->list:
        i = 0
        while(i < len(inputs)):
            times = inputs.count(inputs[i])
            if(times > 1):
                inputs.remove(inputs[i])
            else:
                i = i + 1
        inputs.sort()
        return inputs

while 1:
    try:
        list1 = []
        counts = int(input(""))
        while(counts != 0 ):
            nums = int(input(""))
            list1.append(nums)
            counts = counts - 1
        y = Solution()
        list2 = y.quchong_paixu(list1)
        for i in list2:
            print(i)
    except:
        break