import unittest
from unittest.mock import patch

# import pytest
# from starlette.testclient import TestClient

def add(x, y):
    return x + y


class TestSquare(unittest.TestCase):



    def test_square(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-2, 6), 4)
        self.assertEqual(add(0, 0), 0)

# from app.main import app

# @pytest.fixture(scope="module")
# # def test_app():
# #     client = TestClient(app)
# #     yield client  # testing happens here
