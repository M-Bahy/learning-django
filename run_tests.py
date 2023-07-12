import unittest
import os


def run_tests():
    loader = unittest.TestLoader()
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(tests_dir, pattern="test_*.py")

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = run_tests()
    result = runner.run(test_suite)
