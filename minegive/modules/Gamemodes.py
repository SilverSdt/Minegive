from enum import StrEnum


class Gamemodes(StrEnum):
    """Gamemodes enum for use in the Selector class."""

    SPECTATOR = "spectator"
    SURVIVAL = "survival"
    CREATIVE = "creative"
    ADVENTURE = "adventure"
