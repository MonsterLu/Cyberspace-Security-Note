class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        list1 = ['I','X','C']
        res = 0
        i = 0
        while(i < len(s)):
            if((s[i] in list1) and (i < len(s)-1) and (dict1[s[i+1]] > dict1[s[i]])):
                res = res + dict1[s[i+1]] - dict1[s[i]]
                i = i + 1
            else:
                res = res + dict1[s[i]]
            i = i + 1
        return res

x = "III"
y = Solution()
print(y.romanToInt(x))