import pytest

from src import hello_user, new_function


def test_hello_ivan():
    assert hello_user("Ivan") == "Hello, Ivan!", 'Ivan has failed'


def test_hello_bob():
    assert hello_user("Bob") == "Hello, Bob!"


def test_wrong_hello():
    with pytest.raises(AssertionError):
        assert hello_user("Alice") == "Hello, NotAlice!"


def test_new_func():
    assert new_function(1, 2) == 3, 'new_function has failed'
    assert new_function(1, 1) == 2, 'new_function has failed'
    with pytest.raises(AssertionError):
        assert new_function(1, 2) == 4, 'new_function has failed'


if __name__ == '__main__':
    test_hello_ivan()
    test_hello_bob()
    test_wrong_hello()
    test_new_func()
