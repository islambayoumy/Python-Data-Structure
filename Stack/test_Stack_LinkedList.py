import pytest

from Stack_LinkedList import Stack


@pytest.fixture
def stack(request):
    """Creating a Stack object"""
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(40)
    stack.push(20)
    return stack


def test_push(stack):
    stack.push(90)
    assert 90 == stack.peek.data


def test_pop_from_empty_stack():
    stack = Stack()
    assert not stack.pop()


def test_pop_(stack):
    assert 20 == stack.pop()


def test_pop_last_item():
    stack = Stack()
    stack.push(1)
    assert 1 == stack.pop()


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()


def test_is_not_empty(stack):
    assert not stack.is_empty()


def test_get_peek(stack):
    assert 20 == stack.get_peek()


def test_get_peek_empty_stack():
    stack = Stack()
    assert not stack.get_peek()


def test_stack_len_empty_stack():
    stack = Stack()
    assert 0 == stack.stack_len(stack.peek)


def test_stack_len(stack):
    assert 4 == stack.stack_len(stack.peek)


def test_get_max(stack):
    assert 40 == stack.get_max()


def test_get_max_after_pop_max(stack):
    stack.pop()
    stack.pop()
    assert 30 == stack.get_max()


def test_get_max_empty_stack():
    stack = Stack()
    assert not stack.get_max()
