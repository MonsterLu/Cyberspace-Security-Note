class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = x
        rev = 0
        if(x < 0):
            return False
        while(x1 != 0):
            digit = x1 % 10
            rev = rev * 10 + digit
            x1 = x1 // 10
        print(rev)
        if(rev == x):
            return True
        else:
            return False
x = 121
y = Solution()
print(y.isPalindrome(x))