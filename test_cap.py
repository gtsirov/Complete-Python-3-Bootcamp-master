import unittest
import cap


class TestCap(unittest.TestCase):
    """
    Inherit the unittest TestCase base class
    """

    def test_one_word(self):
        test = 'python'
        result = cap.cap_text(test)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        test = 'monthy python'
        result = cap.cap_text(test)
        self.assertEqual(result, 'Monthy Python')


if __name__ == '__main__':
    unittest.main()
