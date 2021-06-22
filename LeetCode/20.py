class Node():
    def __init__(self,key,value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.front = self

class Link():
    def add_node(self,head:Node,node:Node):
        fake = head
        if(fake.next == None):
            head.next = node
            node.front = head
        else:
            while 1:
                if(fake.next == None):
                    node.next = node
                    node.front = fake
                    break
                else:
                    if(node.key > fake.key):
                        fake = head.next


    def print_link(self,head:Node):
        fake = head
        while 1:
            if(fake.next == None):
                print(fake.key, fake.value)
                break
            print(fake.key, fake.value)
            fake = head.next

head = Node(1,3)
node1 = Node(2,3)
node2 = Node(3,4)

link = Link()
link.add_node(head,node1)
link.add_node(head,node2)
print(head.front,head.next)
print(node1.front,node1.next)
print(node2.front,node2.next)
link.print_link(head)