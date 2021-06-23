class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Link():
    def add_node(self,head:Node,node:Node):
        fake = head
        if(fake.next == None):
            head.next = node
        else:
            while 1:
                if(fake.next == None):
                    fake.next = node
                    break
                elif(node.key > fake.next.key):
                    fake = fake.next
                elif(node.key < fake.next.key):
                    node.next = fake.next
                    fake.next = node
                    break

    def print_link(self,head:Node):
        fake = head.next
        while(fake.next != None):
            print(fake.key,fake.value)
            fake = fake.next
        print(fake.key, fake.value)

x = {}
count = int(input(""))
num = 1
link = Link()
head = Node(-1,count)
while(num <= count):
    keyin = input("")
    keyin1 = keyin.split()
    if(len(keyin1) == 1):
        x[int(keyin1[0])] = 0
    elif(int(keyin1[0]) in x):
        x[int(keyin1[0])] = int(keyin1[1]) + x[int(keyin1[0])]
    else:
        x[int(keyin1[0])] = int(keyin1[1])
    num = num + 1

for item in x:
    #print(item,x[item])
    node = Node(item,x[item])
    #print(node.key,node.value)
    link.add_node(head,node)
link.print_link(head)
#node1 = Node()
#link.add_node(head, node1)

#link.print_link(head)