class Node():
    def __init__(self, data = 0, node = None):
        self.data = data
        self.next = node


class Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head == None or self.size < 1:
            return True
        return False

    def insert(self, n:Node , i:int):
        if type(n) != Node or type(i) != int:
            raise Exception("These datatypes are wrong")
        elif i > self.size:
            raise Exception("index out of range")
        if self.head == None:
            self.head = n
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
        self.isEmpty()
        x = self.head  
        for n in range(0, i-1):  
            x = x.next 
        return x.data 
    
    def delete(self, i):
        self.isEmpty()
        x = self.head 
        for n in range(0, i-1): 
            x = x.next  
        y = x.next  
        x.next = y.next 
        self.size -= 1 

    def de_duplicator(self):
            self.isEmpty()
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

  