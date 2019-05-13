import pytest

from CircularLinkedList import CircularLinkedList


@pytest.fixture
def cllist(request):
    """Creating a LinkedList object"""
    cllist = CircularLinkedList()
    cllist.add_head(3)
    cllist.add_head(2)
    cllist.add_head(1)
    return cllist


def test_is_linkedlist_empty(cllist):
    assert cllist.head, "list is empty"
