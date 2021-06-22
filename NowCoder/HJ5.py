import sys

class Solution:
    def change(self, inputs: str) -> int:
        y = inputs[2:]
        start = len(y) - 1
        sum = 0
        dict1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for i in range(len(y)):
            if (y[i] in dict1):
                sum = sum + dict1[y[i]] * pow(16, start)
            else:
                sum = sum + int(y[i]) * pow(16, start)
            start = start - 1

        return sum

y = Solution()
for line in sys.stdin:
    a = line.split()
    print(a)
    if(a != []):
        print(y.change(a[0]))





