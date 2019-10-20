""" Test Example """
import pytest


@pytest.mark.performance
def test_foo():
    """ This is the foo test """
    assert False


@pytest.mark.high
def test_bar():
    """ This is the bar test """
    assert True


def test_baz():
    """ This is the baz test """
    assert True


# pylint: disable=R0201
class TestFoo():
    """ Test Class for foo """

    @pytest.mark.high
    @pytest.mark.performance
    def test_a(self):
        """ This is the TestFoo.a test
          Make this a multiline testx
        """
        assert False

    def test_b(self):
        """ This is the TestFoo.b test """
        assert True
