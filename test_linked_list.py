#import pytest

from Linked_List import Linked_List, Node

def test_isEmpty_true():
    obj = Linked_List()

    assert obj.isEmpty() == True
    
def test_isEmpty_false():
    obj = Linked_List()
    node = Node(7)

    obj.head = node
    obj.size = 1

    assert obj.isEmpty() == False



def test_insert():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 1)
    obj.insert(n3, 1)
    print(obj.size)
    assert obj.size == 2
    assert obj.head != None
    assert n4.next == n3
