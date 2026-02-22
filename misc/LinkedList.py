class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.next = None
    
    def add_node(self, val: int):
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        
        curr.next = Node(val)
    
    def print_ll(self):
        curr = self.head
        while (curr.next != None):
            print(str(curr.val) + "->", end='')
            curr = curr.next
        print(curr.val)

class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val

if __name__ == '__main__':
    ll = LinkedList()

    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)

    ll.print_ll()