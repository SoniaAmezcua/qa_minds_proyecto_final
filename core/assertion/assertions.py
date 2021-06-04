import pytest

def assert_true(condition,error_message):
    try:
        assert condition
    except AssertionError:
        pytest.fail(error_message)

def assert_false(condition,error_message):
    try:
        assert not condition
    except AssertionError:
        pytest.fail(error_message)

def assert_equal(expected, actual,error_message):
    try:
        assert expected == actual
    except AssertionError:
        pytest.fail(error_message)

def assert_not_equal(expected, actual,error_message):
    try:
        assert expected != actual
    except AssertionError:
        pytest.fail(error_message)