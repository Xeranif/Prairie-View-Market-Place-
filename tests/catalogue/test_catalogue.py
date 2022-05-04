# from django.test import TestCase


# class TestClass(TestCase):
#     def test_hello_world(self):
#         self.assertEqual("Hello", "Hello")

import pytest


@pytest.fixture
def test_fixture1():
    print("Run each test")
    return 1


def test_hello_world(test_fixture1):
    print("function_fixture1")
    assert test_fixture1 == 1
