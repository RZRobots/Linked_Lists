class Node():
    def __init__(self):
        self.data = 0
        self.next = None


class Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def runnable(self):
        if self.head != None and self.tail != None and self.size > 1:
            pass
        else:
            raise Exception("None Error")

    def insert(self, n, i):
        if self.head == None:
            self.head == n
            self.size += 1

        elif self.tail == None:
            self.head.next = n
            self.tail == n
            self.size += 1

        else:
            x = self.head  
            for a in range(0, i-1):  
                x = x.next  
            n.next = x.next
            x.next = n 
            self.size += 1 
    
    def find(self, i):
        x = self.head  
        for n in range(0, i-1):  
            x = x.next 
        return x.data 