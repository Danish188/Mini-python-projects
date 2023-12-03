class Node:
    def __init__(self , data = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def append(self , data):
        new_node = Node(data)
        cur = self.head        
        while cur.next != None:
            cur = cur.next 
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total =0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def get(self, position):
         if position >= self.length():
             return False
         cur_indx = 0
         cur = self.head
         while True:
             cur = cur.next
             if cur_indx == position:
                 return cur.data
             cur_indx+=1
        
my_list = LinkedList()

my_list.append(3)
my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append(7)
my_list.append(5)
my_list.append(9)
my_list.append(0)
my_list.append(1)

my_list.display()

print(my_list.get(3))