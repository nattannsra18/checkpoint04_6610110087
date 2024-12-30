# ฟังก์ชันคำนวณ Fibonacci
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Unit Test
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(4), 2)
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(6), 5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci(0)
        with self.assertRaises(ValueError):
            fibonacci(-5)

if __name__ == "__main__":
    unittest.main()
