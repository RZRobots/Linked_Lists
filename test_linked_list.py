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



