import pytest

from katas.stack_tdd.stack_tdd import Stack


@pytest.fixture()
def stack():
    stack = Stack()
    yield stack
