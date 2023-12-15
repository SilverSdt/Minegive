# <========== Imports ==========>

from __future__ import annotations

# <========== Class ==========>

class ItemNBT:
    """_ItemNBT represents the NBT data for any item in Minecraft.
    """

    def __init__(self: ItemNBT, damage: int | None, unbreakable: bool | None, can_destroy: list[str] | None, custom_model_data: int | None, attribute_modifiers: list[dict] | None = None) -> None:
        """ Constructor of the class

        Args:
            self (ItemNBT): Self
            damage (int | None): The number of uses consumed (not remaining) of the item's durability.
            unbreakable (bool | None): 1 or 0 (true/false) - if true, the item doesn't lose durability when used.
            can_destroy (list[str] | None): The only blocks this item may break when used by a player in adventure mode.
            custom_model_data (int | None): A value used in the "custom_model_data" item tag in the overrides of item models.

            attribute_modifiers (list[dict] | None, optional): A list of attribute modifiers. Defaults to None.
        """
        self.damage: int | None = damage
        self.unbreakable: bool | None = unbreakable
        self.can_destroy: list[str] | None = can_destroy
        self.custom_model_data: int | None = custom_model_data


        if attribute_modifiers != None:
            for value in attribute_modifiers:
                for key in value:
                    if key not in ["AttributeName", "Name", "Slot", "Operation", "Amount", "UUID"]:
                        raise ValueError("AttributeModifiers must only contain AttributeName, Name, Slot, Operation, Amount, and UUID.")

        self.attribute_modifiers: list[dict] | None = attribute_modifiers

    def __dict__(self:ItemNBT) -> dict:
        """ Returns the dictionary representation of the object. This is used when converting the object to JSON.

        Args:
            self (ItemNBT): Self

        Returns:
            dict: Dictionary representation of the object.
        """
        res: dict = {}

        if self.damage != None: res["Damage"] = self.damage
        if self.unbreakable != None: res["Unbreakable"] = self.unbreakable
        if self.can_destroy != None: res["CanDestroy"] = self.can_destroy
        if self.custom_model_data != None: res["CustomModelData"] = self.custom_model_data

        res["AttributeModifiers"] = {}

        if self.attribute_modifiers != None:
            for key, value in enumerate(self.attribute_modifiers):
                res["AttributeModifiers"][key] = value

        return res

    def __str__(self:ItemNBT) -> str:
        """ Returns the string representation of the object.
        This is used when converting the object to a string.

        Args:
            self (ItemNBT): Self

        Returns:
            str: String representation of the object.
        """
        return str(self.__dict__())

    def __repr__(self:ItemNBT) -> str:
        """ Returns the string which is used to recreate the object.
        This is used when converting the object to a string.

        Args:
            self (ItemNBT): Self

        Returns:
            str: String which is used to recreate the object.
        """
        return str(self.__dict__())
