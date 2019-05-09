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

def test_add_before(dllist):
    dllist.add_before(5, 10)
    assert 10 == dllist.get_head().data
