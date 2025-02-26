import unittest


class TestMathOperations(unittest.TestCase):
    def setUp(self):
        # Setup block (optional)
        self.a = 10
        self.b = 5

    def test_addition(self):
        self.assertEqual(self.a + self.b, 15)

    def test_subtraction(self):
        self.assertEqual(self.a - self.b, 5)

    def tearDown(self):
        # Teardown block (optional)
        pass


if __name__ == "__main__":
    unittest.main()
