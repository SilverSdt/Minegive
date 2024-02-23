# <========== Imports ==========>

from __future__ import annotations

# <========== Local Imports ==========>

from minegive.modules.ItemNBT import ItemNBT

# <========== Class ==========>

class BlockNBT(ItemNBT):
    """ The NBT of a block. Inherits from ItemNBT.
    """

    def __init__(self: BlockNBT, damage: int | None = None, unbreakable: bool | None = None, can_destroy: list[str] | None = None, custom_model_data: int | None = None, attribute_modifiers: list[dict] | None = None,
                can_place_on: list[str] | None = None, block_entity_tag: dict | None = None, block_state_tag: dict | None = None) -> None:
        """ The init method of the BlockNBT class.

        Args:
            self (BlockNBT): Self
            damage (int | None): the damage of the block. Defaults to None.
            unbreakable (bool | None): the unbreakable of the block. Defaults to None.
            can_destroy (list[str] | None): if the block can be destroyed. Defaults to None.
            custom_model_data (int | None): the custom model data of the block. Defaults to None.
            attribute_modifiers (list[dict] | None, optional): attribute modifiers of the block. Defaults to None.

            can_place_on (list[str] | None, optional): on what blocks the block can be placed. Defaults to None.
            block_entity_tag (dict | None, optional): dict of the block entity tag. Defaults to None.
            block_state_tag (dict | None, optional): dict of the block state tag. Defaults to None.
        """
        super().__init__(damage, unbreakable, can_destroy, custom_model_data, attribute_modifiers)

        self.can_place_on: list[str] | None = can_place_on
        self.block_entity_tag: dict | None = block_entity_tag
        self.block_state_tag: dict | None = block_state_tag

    def __dict__(self: BlockNBT) -> dict:
        """ The dict method of the BlockNBT class.

        Args:
            self (BlockNBT): Self

        Returns:
            dict: The dict of the BlockNBT class.
        """
        res: dict = super().__dict__()

        if self.can_place_on is not None: res["CanPlaceOn"] = self.can_place_on
        if self.block_entity_tag is not None: res["BlockEntityTag"] = self.block_entity_tag
        if self.block_state_tag is not None: res["BlockStateTag"] = self.block_state_tag

        return res

    def __str__(self: BlockNBT) -> str:
        """ The str method of the BlockNBT class.
        Returns the dict as a string.

        Args:
            self (BlockNBT): Self

        Returns:
            str: The dict as a string.
        """
        return str(self.__dict__())

    def __repr__(self: BlockNBT) -> str:
        """ The repr method of the BlockNBT class.

        Args:
            self (BlockNBT): Self

        Returns:
            str: The dict as a string.
        """
        return str(self.__dict__())