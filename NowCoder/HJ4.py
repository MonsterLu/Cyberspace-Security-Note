#字符串分隔
def buzero(inputs:str):
    chazhi = 8 - len(inputs)
    res = inputs + '0' *chazhi
    print(res)

def ganghao(inputs:str):
    print(inputs)

def fenge(inputs:str):
    length = len(inputs)
    if (length < 8):
        buzero(inputs)

    elif(length == 8):
        ganghao(inputs)

    elif(length > 8):
        small1 = inputs[:8]
        num = len(small1)
        if(num == 8):
            ganghao(small1)
        else:
            buzero(small1)
        inputs = inputs[8:]
        fenge(inputs)

while True:
    try:
        words = input("")
        x = fenge(words)
    except:
        break