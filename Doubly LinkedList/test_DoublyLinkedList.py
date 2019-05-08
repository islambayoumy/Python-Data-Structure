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

def test_add_to_tail(dllist):
    dllist.add_tail(100)
    assert 100 == dllist.get_tail().data, "not a tail"
