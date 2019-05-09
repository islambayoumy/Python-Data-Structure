import pytest

from DoublyLinkedList import DoublyLinkedList

@pytest.fixture
def dllist(request):
    """Creating a DoublyLinkedList object"""
    dllist = DoublyLinkedList()
    dllist.add_tail(5)
    dllist.add_tail(6)
    dllist.add_tail(7)
    return dllist

# just for coverage
def test_print_list(dllist):
    assert not dllist.print_list()

def test_is_linkedlist_empty(dllist):
    assert dllist.head, "list is empty"

def test_list_count(dllist):
    assert 3 == dllist.list_count(dllist.head)

def test_add_to_empty_list():
    dllist = DoublyLinkedList()
    dllist.add_head(1)
    assert 1 == dllist.get_head().data

def test_add_to_head(dllist):
    dllist.add_head(1)
    assert 1 == dllist.get_head().data, "not a head"

def test_add_to_tail(dllist):
    dllist.add_tail(100)
    assert 100 == dllist.get_tail().data, "not a tail"

def test_add_after(dllist):
    dllist.add_after(7, 10)
    assert 10 == dllist.get_tail().data

def test_add_after_not_tail(dllist):
    count = dllist.list_count(dllist.head)
    dllist.add_after(6, 10)
    assert count+1 == dllist.list_count(dllist.head)

def test_add_before(dllist):
    dllist.add_before(5, 10)
    assert 10 == dllist.get_head().data

def test_add_before_not_head(dllist):
    count = dllist.list_count(dllist.head)
    dllist.add_before(6, 10)
    assert count+1 == dllist.list_count(dllist.head)

def test_delete_node_head_only():
    dllist = DoublyLinkedList()
    dllist.add_head(1)
    dllist.delete_node(1)
    assert 0 == dllist.list_count(dllist.head)

def test_delete_node_head(dllist):
    count = dllist.list_count(dllist.head)
    dllist.delete_node(5)
    assert count-1 == dllist.list_count(dllist.head)
    
def test_delete_node(dllist):
    count = dllist.list_count(dllist.head)
    dllist.delete_node(6)
    assert count-1 == dllist.list_count(dllist.head)
    
def test_delete_node_tail(dllist):
    count = dllist.list_count(dllist.head)
    dllist.delete_node(7)
    assert count-1 == dllist.list_count(dllist.head)

def test_reverse_list(dllist):
    tail = dllist.get_tail()
    dllist.reverse_list()
    assert tail == dllist.get_head()
