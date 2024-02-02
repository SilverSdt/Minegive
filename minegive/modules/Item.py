from minegive.modules.ItemID import ItemID
from minegive.modules.ItemNBT import ItemNBT


class Item:
    """Represents a minecraft item."""

    def __init__(self, item: ItemID, nbt: ItemNBT | None = None, quantity: int = 1):
        """Initializes a new instance of the Item class.

        Args:
            item (ItemID): ID of the item.
            nbt (ItemNBT, optional): NBT data of the item. Defaults to None.
            quantity (int, optional): Quantity of the item. Defaults to 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > 2147483647:
            raise ValueError("Quantity must be less than 2147483647")

        self.item = item
        self.nbt = nbt or ItemNBT()
        self._quantity = quantity

    @property
    def quantity(self) -> int:
        """Returns the quantity of the item.

        Returns:
            int: Quantity of the item.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """Sets the quantity of the item.

        Args:
            value (int): Quantity of the item.
        """
        if value < 1:
            raise ValueError("Quantity must be greater than 0")
        elif value > 2147483647:
            raise ValueError("Quantity must be less than 2147483647")
        self._quantity = value

    def __eq__(self, o: object) -> bool:
        """Returns whether the item is equal to another item.

        Args:
            o (object): Object to compare.

        Returns:
            bool: Whether the item is equal to another item.
        """
        if not isinstance(o, Item):
            return False
        return self.item == o.item and self.nbt == o.nbt and self.quantity == o.quantity

    def __str__(self) -> str:
        """Returns the string representation of the item.

        Returns:
            str: String representation of the item.
        """
        return f"{self.item}{self.nbt} {self.quantity}"

    def __repr__(self) -> str:
        """Returns the string representation of the item.

        Returns:
            str: String representation of the item.
        """
        return f"Item({self.item}, {self.nbt}, {self.quantity})"
