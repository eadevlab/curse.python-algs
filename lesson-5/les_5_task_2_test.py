import unittest

from les_5_task_2 import HexNumber


class TestTask2(unittest.TestCase):
    def setUp(self) -> None:
        self.hex_num_1 = 'A2'
        self.hex_num_2 = 'C4F'

    def test_add(self):
        test_sum = hex(int(self.hex_num_1, 16) + int(self.hex_num_2, 16))
        a = HexNumber(self.hex_num_1)
        b = HexNumber(self.hex_num_2)
        self.assertEqual(str(test_sum)[2:].upper(), str(a+b))

    def test_multiple(self):
        test_mul = hex(int(self.hex_num_1, 16) * int(self.hex_num_2, 16))
        a = HexNumber(self.hex_num_1)
        b = HexNumber(self.hex_num_2)
        self.assertEqual(str(test_mul)[2:].upper(), str(a*b))


if __name__ == '__main__':
    unittest.main()
