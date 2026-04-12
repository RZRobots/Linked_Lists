class Node():
    def __init__(self, data = 0, node = None):
        self.data = data
        self.next = node


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
        self.runnable()
        x = self.head  
        for n in range(0, i-1):  
            x = x.next 
        return x.data 
    
    def delete(self, i):
        self.runnable()
        x = self.head 
        for n in range(0, i-1): 
            x = x.next  
        y = x.next  
        x.next = y.next 
        self.size -= 1 

    def de_duplicator(self):
            self.runnable()
            x = self.head
            y = x.next
            i = 1
            while y.next != None:
                if x.data == y.data and i < self.size:
                    self.delete(i)
                else:
                    self.delete(i)
                    self.tail = x
                i+=1
                x = x.next
                y = x.next

  