from greetings import greet, farewell


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_farewell():
    assert farewell("Ada") == "Goodbye, Ada!"
