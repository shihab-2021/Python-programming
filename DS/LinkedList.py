from pprint import pprint


class Node:
    def __init__(self, v):
        self.val = v
        self.next = None 

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, pos, val):
        newNode = Node(val)
        if pos==0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
                if temp == None:
                    print("Out of bound")
                    return 
            newNode.next = temp.next
            temp.next = newNode

    def insert_at_tail(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def delete_at_pos(self, pos):
        if pos==0:
            delNode = self.head
            self.head = self.head.next
            del delNode
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
                if temp == None:
                    print("Out of bound")
                    return 
            delNode = temp.next
            if temp.next == None:
                print("Out of bound")
                return 
            temp.next = temp.next.next
            del delNode 

    def reverse(self):
        if self.head.next == None:
            return self.head
        save = self.head
        self.head = self.head.next
        newHead = self.reverse()
        save.next.next = save
        save.next = None
        return newHead
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next

def main():
    lst = Linked_list()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.insert_at_pos(1, 40)
    lst.print_list()
    lst.delete_at_pos(1)
    lst.print_list()

main()