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


#Delete this once all insert positive tests are done
# def test_insert_p():
#     obj = Linked_List()
#     n4 = Node(8)
#     n3 = Node(9)
#     n2 = Node(7)
#     obj.insert(n4, 0) 
#     obj.insert(n3, 0)
#     obj.insert(n2, 1)
#     assert obj.size == 3
#     assert obj.head == n3
#     assert obj.find(1) == 7
#     assert obj.tail == n4
#     assert n3.next == n2

def test_insert_p_empty():
    obj = Linked_List()
    n1 = Node(1)
    obj.insert(n1, 0)
    assert obj.size == 1
    assert obj.head == n1
    assert obj.find(0) == 1
    assert obj.tail == n1
    assert n1.next == None

def test_insert_p_full():
    obj = Linked_List()
    n1 = Node(1)
    n2 = Node(2)
    obj.head = n1
    obj.tail = n1
    obj.size = 1
    obj.insert(n2, 1)
    assert obj.size == 2
    assert obj.head == n1
    assert obj.find(1) == 2
    assert obj.tail == n2
    assert n1.next == n2

def test_insert_p_head():
    obj = Linked_List()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    obj.head = n1
    obj.tail = n2
    obj.size = 2
    n1.next = n2
    obj.insert(n3, 0)
    assert obj.size == 3
    assert obj.head == n3
    assert obj.find(1) == 1
    assert obj.tail == n2
    assert n3.next == n1

def test_insert_p_tail():
    obj = Linked_List()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    obj.head = n1
    obj.tail = n2
    obj.size = 2
    n1.next = n2
    obj.insert(n3, 2)
    assert obj.size == 3
    assert obj.head == n1
    assert obj.find(1) == 2
    assert obj.tail == n3
    assert n3.next == None
    assert n2.next == n3

def test_insert_p_middle():
    obj = Linked_List()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    obj.head = n1
    obj.tail = n2
    obj.size = 2
    n1.next = n2
    obj.insert(n3, 1)
    assert obj.size == 3
    assert obj.head == n1
    assert obj.find(1) == 3
    assert obj.tail == n2
    assert n3.next == n2
    assert n1.next == n3

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
    with pytest.raises(TypeError):
        obj.insert(2, n3)

def test_insert_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(TypeError):
        obj.insert("n3", "")

def test_insert_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(IndexError):
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
    with pytest.raises(TypeError):
        obj.delete()

def test_delete_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(TypeError):
        obj.delete("5")

def test_delete_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(AttributeError):
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
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        obj.find()

def test_find_typeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(TypeError):
        obj.find(n3)

def test_find_rangeError():
    obj = Linked_List()
    n4 = Node(8)
    n3 = Node(9)
    with pytest.raises(AttributeError):
        obj.find(10)


