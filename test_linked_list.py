import pytest

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



def test_insert_p():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    assert obj.size == 2
    assert obj.head != None
    assert n4.next == n3

def test_insert_empty():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(TypeError):
        obj.insert()

def test_insert_flipped():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.insert(2, n3)

def test_insert_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.insert("n3", "")

def test_insert_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.insert(n3, 10)

def test_delete_p():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    obj.delete(1)
    assert n4.next == None


def test_delete_empty():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    with pytest.raises(Exception):
        obj.delete()

def test_delete_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.delete("5")

def test_delete_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.delete(10)

def test_de_duplicator_p():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    obj.de_duplicator()
    assert n3.next == None

def test_de_duplicator_attributeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    with pytest.raises(Exception):
        obj.de_duplicator("5")

def test_find_p():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    assert obj.find(0) == 8
    
def test_find_empty():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    obj.insert(n4, 0)
    obj.insert(n3, 1)
    with pytest.raises(Exception):
        obj.find()

def test_find_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.find(n3)

def test_find_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(Exception):
        obj.find(10)


