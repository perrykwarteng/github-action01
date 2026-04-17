from main import add_numbers, get_app_info


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_negative_numbers():
    assert add_numbers(-1, -1) == -2


def test_add_zero():
    assert add_numbers(0, 5) == 5


def test_app_info():
    result = get_app_info()
    assert isinstance(result, str)
    assert "running in" in result