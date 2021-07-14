def do_command(inputs:list)->list:
    dict1 = ['A','W','S','D']
    dict2 = ['0','1','2','3','4','5','6','7','8','9']
    print(inputs)
    for item in inputs:
        if (item == ''):
            inputs.remove(item)
            continue
        if((len(item) > 3) or (item[0] not in dict1)or (item[1] not in dict1)):
            print(item,"不符合1")
            inputs.remove(item)
            continue

        if(len(item) >=  2):
            if (item[1] not in dict2):
                print(item, "不符合2")
                inputs.remove(item)
                continue
        if(len(item) == 3):
            if(item[2] not in dict2):
                print(item, "不符合2")
                inputs.remove(item)
                continue


    return inputs

class Origin():
    def __init__(self):
        self.x = 0
        self.y = 0

o = Origin()

#while True:
  #  try:
command = input("")
list1 = command.split(";")
list1 = do_command(list1)

print(list1)

  #  except:
   #     break