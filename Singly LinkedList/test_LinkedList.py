import pytest

from LinkedList import LinkedList

@pytest.fixture
def llist(request):
    """Creating a LinkedList object"""
    llist = LinkedList()
    llist.add_head("M")
    llist.add_head("N")
    llist.add_head("O")
    return llist

def test_is_linkedlist_empty(llist):
    assert llist.head, "list is empty"

def test_add_to_head(llist):
    llist.add_head("A")
    assert "A" == llist.get_head().data, "not a head"

def test_add_to_tail(llist):
    llist.add_tail("Z")
    assert "Z" == llist.get_tail().data, "not a tail"

def test_add_to_position(llist):
    llist.add_node("E", 2)
    assert "E" == llist.get_node_by_position(2).data

def test_get_node_by_position(llist):
    assert llist.get_node_by_data("N") == llist.get_node_by_position(2)

def test_get_node_by_position_out_of_range(llist):
    assert llist.get_tail() == llist.get_node_by_position(1000)

def test_get_position_of_node_by_data(llist):
    assert 2 == llist.get_position_of_node_by_data("N")

def test_get_position_of_node_by_data_not_exist(llist):
    assert not llist.get_position_of_node_by_data("Not")

def test_get_node_by_data(llist):
    assert "O" == llist.get_node_by_data("O").data

def test_get_node_by_data_not_exist(llist):
    assert not llist.get_node_by_data("Not")

def test_delete_head_get_new_head(llist):
    new_head = llist.delete_head()
    assert new_head == llist.get_head()

def test_delete_head_list_count(llist):
    list_count = llist.list_count(llist.head)
    llist.delete_head()
    assert list_count - 1 == llist.list_count(llist.head)

def test_delete_by_position_is_the_head(llist):
    new_head = llist.delete_by_position(0)
    assert new_head == llist.get_head()

def test_delete_by_position_list_count(llist):
    list_count = llist.list_count(llist.head)
    llist.delete_by_position(3)
    assert list_count - 1 == llist.list_count(llist.head)

def test_delete_by_data_is_the_head(llist):
    new_head = llist.delete_by_data("O")
    assert new_head == llist.get_head()

def test_delete_by_data_list_count(llist):
    list_count = llist.list_count(llist.head)
    llist.delete_by_data("M")
    assert list_count - 1 == llist.list_count(llist.head)

def test_reverse_list_iterative(llist):
    tail = llist.get_tail()
    llist.reverse_list_iterative()
    assert tail == llist.get_head()

def test_reverse_list_recursive(llist):
    tail = llist.get_tail()
    llist.reverse_list_recursive()
    assert tail == llist.get_head()

def test_swap_nodes_same_node(llist):
    old_pos = llist.get_position_of_node_by_data("O")
    llist.swap_nodes("O", "O")
    new_pos = llist.get_position_of_node_by_data("O")
    assert old_pos == new_pos

def test_swap_nodes_head_node_left(llist):
    llist.swap_nodes("O", "M")
    assert llist.get_node_by_data("M") == llist.get_head()

def test_swap_nodes_head_node_right(llist):
    llist.swap_nodes("M", "O")
    assert llist.get_node_by_data("M") == llist.get_head()

def test_swap_nodes(llist):
    old_pos = llist.get_position_of_node_by_data("N")
    llist.swap_nodes("N", "M")
    new_pos = llist.get_position_of_node_by_data("M")
    assert old_pos == new_pos

def test_swap_nodes_not_exist(llist):
    assert not llist.swap_nodes("A", "M")
