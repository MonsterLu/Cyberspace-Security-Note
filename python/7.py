class Solution:
    def reverse(self, x: int) -> int:
        x1 = x
        rev = 0
        x2 = abs(x)
        while(x2 != 0):
            digit = x2 % 10
            rev = rev * 10 + digit
            x2 = x2 // 10
        print(rev)
        if(-2147483648 <= rev <= 2147483647):
            if (x1 < 0):
                return -rev
            else:
                return rev
        else:
            return 0
x=1534236469
y = Solution()
print(y.reverse(x))