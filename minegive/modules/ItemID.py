class ItemID:
    """Represents a minecraft item ID."""

    def __init__(self, item: str = "stone", namespace: str = "minecraft"):
        """Initializes a new instance of the ItemID class.

        Args:
            item (str, optional): Name of the item. Defaults to "stone".
            namespace (str, optional): Namespace of the item. Defaults to "minecraft".
        """
        self.namespace = namespace
        self.item = item

    def __eq__(self, o: object) -> bool:
        """Returns whether the item ID is equal to another item ID.

        Args:
            o (object): Object to compare.

        Returns:
            bool: Whether the item ID is equal to another item ID.
        """
        if not isinstance(o, ItemID):
            return False
        return self.namespace == o.namespace and self.item == o.item

    def __str__(self) -> str:
        """Returns the string representation of the item ID.

        Returns:
            str: String representation of the item ID.
        """
        return f"{self.namespace}:{self.item}"

    def __repr__(self) -> str:
        """Returns the string representation of the item ID.

        Returns:
            str: String representation of the item ID.
        """
        return f"ItemID({self.item}, {self.namespace})"
