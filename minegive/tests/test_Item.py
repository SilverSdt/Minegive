import unittest

from minegive.modules.Item import Item
from minegive.modules.ItemID import ItemID
from minegive.modules.ItemNBT import ItemNBT


class TestItem(unittest.TestCase):
    def test_init(self):
        item_id = ItemID("apple", "minecraft")
        item = Item(item_id, quantity=10)
        self.assertEqual(item.item, item_id)
        self.assertEqual(item.nbt, ItemNBT())
        self.assertEqual(item.quantity, 10)

    def test_quantity_setter(self):
        item_id = ItemID("apple", "minecraft")
        item = Item(item_id, quantity=10)
        with self.assertRaises(ValueError):
            item.quantity = 0  # Quantity must be greater than 0
        with self.assertRaises(ValueError):
            item.quantity = 2147483648  # Quantity must be less than 2147483647
        item.quantity = 5
        self.assertEqual(item.quantity, 5)

    def test_str(self):
        item_id = ItemID("apple", "minecraft")
        item = Item(item_id, quantity=10)
        self.assertEqual(str(item), "minecraft:apple{} 10")


if __name__ == "__main__":
    unittest.main()
