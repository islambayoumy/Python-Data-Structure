import pytest

from DoublyLinkedList import DoublyLinkedList

@pytest.fixture
def dllist(request):
    """Creating a DoublyLinkedList object"""
    dllist = DoublyLinkedList()
    return dllist

# just for coverage
def test_print_list(dllist):
    assert not dllist.print_list()
