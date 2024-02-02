import unittest

from minegive.modules.ItemID import ItemID


class TestItemID(unittest.TestCase):
    def test_init(self):
        item = ItemID("apple", "minecraft")
        self.assertEqual(item.item, "apple")
        self.assertEqual(item.namespace, "minecraft")

    def test_eq(self):
        item1 = ItemID("apple", "minecraft")
        item2 = ItemID("apple", "minecraft")
        item3 = ItemID("stone", "minecraft")
        self.assertTrue(item1 == item2)
        self.assertFalse(item1 == item3)

    def test_str(self):
        item = ItemID("apple", "minecraft")
        self.assertEqual(str(item), "minecraft:apple")

    def test_repr(self):
        item = ItemID("apple", "minecraft")
        self.assertEqual(repr(item), "ItemID(apple, minecraft)")


if __name__ == "__main__":
    unittest.main()
