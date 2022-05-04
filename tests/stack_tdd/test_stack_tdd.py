from pytest import raises

from tests.stack_tdd.stack_fixture import stack

from katas.stack_tdd.stack_tdd import StackUnderflowException


def test_new_stack_is_empty(stack):
    assert stack.is_empty() is True


def test_after_one_push_stack_is_not_empty(stack):
    stack.push(0)
    assert stack.is_empty() is False


def test_pop_empty_stack_returns_underflow_exception(stack):
    with raises(StackUnderflowException):
        stack.pop()


def test_after_one_push_one_pop_new_stack_is_empty(stack):
    stack.push(0)
    stack.pop()
    assert stack.is_empty() is True


def test_push_twice_pop_once_stack_size_is_one(stack):
    stack.push(0)
    stack.push(0)
    stack.pop()
    assert stack.is_empty() is False


def test_push_x_pop_x_equals_x(stack):
    stack.push(99)
    assert stack.pop() == 99
    stack.push(88)
    assert stack.pop() == 88


def test_push_x_then_y_pop_y_then_x(stack):
    stack.push(99)
    stack.push(88)
    assert stack.pop() == 88
    assert stack.pop() == 99


def test_push_out_of_range_elements_does_not_raise_exception(stack):
    stack.push(99)
    stack.push(88)
    stack.push(77)
