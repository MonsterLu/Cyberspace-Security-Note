#句子逆序
word = input("")
list1 = word.split()
length = len(list1)
i = 0
while(i < length):
    print(list1.pop(),end=" ")
    i = i + 1
