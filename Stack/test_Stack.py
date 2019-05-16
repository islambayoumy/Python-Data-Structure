import pytest

from Stack import Stack


@pytest.fixture
def stack(request):
    """Creating a Stack object"""
    stack = Stack()
    return stack


def test_push(stack):
    stack.push(10)
    assert 1 == len(stack.items)


def test_pop_empty(stack):
    assert not stack.pop()


def test_pop_empty(stack):
    stack.push(10)
    assert 10 == stack.pop()


def test_is_empty(stack):
    assert stack.is_empty()


def test_is_not_empty(stack):
    stack.push(10)
    assert not stack.is_empty()


def test_stack_length(stack):
    stack.push(10)
    stack.push(11)
    assert 2 == stack.get_length()


def test_get_peek(stack):
    stack.push(10)
    stack.push(11)
    assert 11 == stack.get_peek()


def test_get_peek_empty_stack(stack):
    assert not stack.get_peek()


def test_get_max(stack):
    stack.push(1)
    stack.push(5)
    stack.push(3)
    stack.push(2)
    assert 5 == stack.get_max()
