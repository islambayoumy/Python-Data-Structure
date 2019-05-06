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

@pytest.fixture
def sorted_llist1(request):
    """Creating a sorted LinkedList object"""
    sorted_llist1 = LinkedList()
    sorted_llist1.add_tail(3)
    sorted_llist1.add_tail(5)
    sorted_llist1.add_tail(7)
    sorted_llist1.add_tail(8)
    return sorted_llist1

@pytest.fixture
def sorted_llist2(request):
    """Creating a sorted LinkedList object"""
    sorted_llist2 = LinkedList()
    sorted_llist2.add_tail(1)
    sorted_llist2.add_tail(2)
    sorted_llist2.add_tail(6)
    sorted_llist2.add_tail(10)
    sorted_llist2.add_tail(12)
    return sorted_llist2

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

def test_merge_two_sorted_lists(sorted_llist1, sorted_llist2):
    new_merged_list = sorted_llist1.merge_two_sorted_lists(sorted_llist2)
    assert new_merged_list.data == 1

def test_merge_two_sorted_lists_reverse(sorted_llist1, sorted_llist2):
    new_merged_list = sorted_llist2.merge_two_sorted_lists(sorted_llist1)
    assert new_merged_list.data == 1

def test_merge_two_sorted_lists_left_empty(sorted_llist1):
    list2 = LinkedList()
    new_merged_list = sorted_llist1.merge_two_sorted_lists(list2)
    assert new_merged_list.data == sorted_llist1.get_head().data

def test_merge_two_sorted_lists_right_empty(sorted_llist2):
    list1 = LinkedList()
    new_merged_list = list1.merge_two_sorted_lists(sorted_llist2)
    assert new_merged_list.data == sorted_llist2.get_head().data

def test_remove_duplicates(llist):
    llist.add_tail("O")
    count = llist.list_count(llist.head)
    llist.remove_duplicates()
    assert llist.list_count(llist.head) == count - 1

def test_compare_two_lists_is_equal_empty():
    llist1 = LinkedList()
    llist2 = LinkedList()
    result = llist1.compare_two_lists_is_equal(llist2.head)
    assert result == 1

def test_compare_two_lists_is_equal_not_same_len(sorted_llist1, sorted_llist2):
    result = sorted_llist1.compare_two_lists_is_equal(sorted_llist2.head)
    assert result == 0

def test_compare_two_lists_is_equal_true(llist):
    result = llist.compare_two_lists_is_equal(llist.head)
    assert result == 1

def test_compare_two_lists_is_equal_false(llist):
    llist1 = LinkedList()
    llist1.add_head("M")
    llist1.add_head("C")
    llist1.add_head("O")
    result = llist.compare_two_lists_is_equal(llist1.head)
    assert result == 0

def test_count_occurence(llist):
    llist.add_tail("O")
    assert llist.count_occurence("O") == 2

def test_rotate_list(llist):
    llist.rotate_list(2)
    assert llist.get_head().data == "M"

def test_is_palindrome(llist):
    assert not llist.is_palindrome()

# just for coverage
def test_print_list(llist):
    assert not llist.print_list()
