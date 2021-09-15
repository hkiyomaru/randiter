import os

from randiter import __version__
from randiter import randiter


here = os.path.dirname(__file__)


def test_version():
    assert __version__ == '0.1.0'


def test_randiter_list():
    list_ = list(range(10))
    assert list_ == sorted(elem for elem in randiter(list_))


def test_randiter_tuple():
    tuple_ = tuple(range(10))
    assert tuple_ == tuple(sorted(elem for elem in randiter(tuple_)))


def test_randiter_set():
    set_ = set(range(10))
    assert set_ == {elem for elem in randiter(set_)}


def test_randiter_str():
    str_ = "abcdefg"
    assert str_ == "".join(sorted(elem for elem in randiter(str_)))


def test_randiter_file():
    with open(os.path.join(here, "test.txt"), "rt") as f:
        lines = sorted(line for line in f)
    with open(os.path.join(here, "test.txt"), "rt") as f:
        assert lines == sorted(elem for elem in randiter(f))
