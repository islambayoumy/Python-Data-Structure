import pytest

from DoublyLinkedList import DoublyLinkedListNode

@pytest.fixture
def llistnode(request):
    """Creating a DoublyLinkedListNode object"""
    llistnode = DoublyLinkedListNode("Test")
    return llistnode

def test_get_data(llistnode):
    assert llistnode.get_data()

def test_get_next(llistnode):
    assert not llistnode.get_next()

def test_get_previous(llistnode):
    assert not llistnode.get_previous()
