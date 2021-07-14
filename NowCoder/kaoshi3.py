class Cell():
    def __init__(self,name:str,flag:int = 1):
        self.name = name
        self.flag = flag
        self.next = None

class Link():
    def connect(self,head:Cell,cell:Cell):
        fake = head
        if(fake.next == None):
            head.next = cell
        else:
            while(fake.next != None):
                fake = fake.next
            fake.next = cell

    def output(self,head):
        fake = head
        while(fake.next != None):
            print(fake.name,fake.flag)
            fake = fake.next
        print(fake.name,fake.flag)

    def bad(self,head,bad:str)->bool:
        fake = head
        while(fake.next != None):
            if(fake.name == bad):
                fake.flag = 0
                return True
            fake = fake.next
        if (fake.name == bad):
            fake.flag = 0
            return True

    def res(self,head)->list:
        res = []
        fake = head.next
        while(fake.next != None):
            #print(fake.name)
            if(fake.flag == 0):
                res = []
            else:
                res.append(fake.name)
            fake = fake.next
            #print(res)
        #print(fake.name)
        if(fake.flag == 0):
            res = []
        if (fake.flag == 1):
            res.append(fake.name)

        return res

ans = []
link1 = Link()
service = input().split(",")
count = len(service)

badsservice = input().split(",")
count1 = len(badsservice)

for i in service:
    head = Cell("head")
    #print(i)
    small = i.split('-')
    #print(small)
    num = len(small)
    j = 0
    while(j < num):
        #print(j)
        cell = Cell(small[j])
        link1.connect(head,cell)
        j = j + 1
    #link1.output(head)
    for i in badsservice:
        link1.bad(head,i)
            #print("flag changed")
    ans = link1.res(head)
    #link1.output(head)


if(len(ans)==0):
    print(",")
else:
    print(','.join(set(ans)))