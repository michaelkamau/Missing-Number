import  unittest
from missing_number_src.missing_number import find_missing


class MissingNumberTest(unittest.TestCase):
    """docstring for MissingNumberTest"""

    def test_empty_list(self):
        self.assertEqual(0, find_missing([], []),
                         msg='should return 0 for empty list')