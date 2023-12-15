import unittest

from minegive.modules.ArgumentTypes import IntRange


class TestIntRange(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            IntRange(None, None)
        self.assertEqual(str(IntRange(1, None)), "1..")
        self.assertEqual(str(IntRange(None, 10)), "..10")
        self.assertEqual(str(IntRange(1, 10)), "1..10")

    def test_start_end_setters(self):
        range = IntRange(1, 10)
        range.start = 2
        self.assertEqual(str(range), "2..10")
        range.end = 8
        self.assertEqual(str(range), "2..8")
        with self.assertRaises(ValueError):
            range.start = None
            range.end = None
            print(range)


if __name__ == "__main__":
    unittest.main()
