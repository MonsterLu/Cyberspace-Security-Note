class Solution:
    def twoSum(self,nums,target)->list:
        for i in range (len(nums)):
            cha = target - nums[i]
            if cha in nums:
                j1 = nums.index(cha,i,len(nums))
                if(j1 >= 0 and j1 != i):
                    return [i,j1]
                j2 = nums.index(cha,0,len(nums))
                if (j1 >= 0 and j2 != i):
                    return [i, j2]
                #for j in range (0,len(nums)):
                #    if ((nums[j] == cha) and (i != j)):
                #return [i,j]

nums = [3,3]
target = 6
list1 = Solution()
print(list1.twoSum(nums,target))








