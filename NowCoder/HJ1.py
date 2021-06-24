#字符串最后一个单词的长度
word = input("")
list1 = word.split()
max = len(list1)
print(len(list1[max-1]))