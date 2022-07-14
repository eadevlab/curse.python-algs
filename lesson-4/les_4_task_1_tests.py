import unittest

import les_4_task_1_1
import les_4_task_1_2
import les_4_task_1_3


class TestTask1(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list = [4, 4, 9, 3, 2, 2, 1]
        self.test_sum = 3 + 2 + 2

    def test_v1(self):
        self.assertEqual(les_4_task_1_1.sum_between_min_max(self.test_list), self.test_sum)

    def test_v2(self):
        self.assertEqual(les_4_task_1_2.sum_between_min_max(self.test_list), self.test_sum)

    def test_v3(self):
        self.assertEqual(les_4_task_1_3.sum_between_min_max(self.test_list), self.test_sum)


if __name__ == '__main__':
    unittest.main()
