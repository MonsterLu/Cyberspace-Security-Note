def search(array,i,j,char)->list:
    l = []
    if(array[i][j-1] == char):
        l.append(i)
        l.append(j)
        return l
    if (array[i][j + 1] == char):
        l.append(i)
        l.append(j)
        return l
    if (array[i - 1][j] == char):
        l.append(i)
        l.append(j)
        return l
    if (array[i+1][j] == char):
        l.append(i)
        l.append(j)
        return l

def start(array,str):
    length = len(array)
    length_str = len(str)
    h = 1
    flag = 0
    for i in range(length):
        for j in range(length):
            if array[i][j] == str[0]:
                list1 = search(array, i, j, str[i])
                while(h < length_str):
                    list2 = search(array, list1[0], list1[1], str[h + 1])
                    if list2 != None:
                        flag = 1
                    if list2 == None:
                        flag = 0
                    h = h + 1
