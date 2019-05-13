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


def test_add_to_head(cllist):
    cllist.add_head(0)
    assert 0 == cllist.get_head().data, "not a head"


def test_add_to_tail(cllist):
    cllist.add_tail(5)
    assert 5 == cllist.get_tail().data, "not a tail"


def test_add_to_tail_empty_list():
    cllist = CircularLinkedList()
    cllist.add_tail(1)
    assert 1 == cllist.get_tail().data


def test_list_count(cllist):
    assert 3 == cllist.list_count()


def test_list_count_empty_list():
    cllist = CircularLinkedList()
    assert 0 == cllist.list_count()


def test_delete_node_head(cllist):
    count = cllist.list_count()
    cllist.delete_node(1)
    assert count-1 == cllist.list_count()


def test_delete_node(cllist):
    count = cllist.list_count()
    cllist.delete_node(2)
    assert count-1 == cllist.list_count()


def test_has_cycle_empty_list():
    cllist = CircularLinkedList()
    assert not cllist.has_cycle()


def test_has_cycle(cllist):
    assert cllist.has_cycle()


def test_has_cycle_head_only():
    cllist = CircularLinkedList()
    cllist.add_head(1)
    cllist.head.next = None
    assert not cllist.has_cycle()


def test_split_list_from_head(cllist):
    h1, h2 = cllist.split_list(1)
    assert 1 == h1.data
    assert 2 == h2.data


def test_split_list(cllist):
    h1, h2 = cllist.split_list(3)
    assert 1 == h1.data
    assert 3 == h2.data
