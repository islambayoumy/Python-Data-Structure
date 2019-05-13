import pytest

from LinkedList import LinkedListNode


@pytest.fixture
def llistnode(request):
    """Creating a LinkedListNode object"""
    llistnode = LinkedListNode("Test")
    return llistnode


def test_get_data(llistnode):
    assert llistnode.get_data()


def test_get_next(llistnode):
    assert not llistnode.get_next()
