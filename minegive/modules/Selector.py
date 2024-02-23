from minegive.modules.ArgumentTypes import IntRange
from minegive.modules.Gamemodes import Gamemodes


class Selector:
    """Represents a selector.
    See https://minecraft.fandom.com/wiki/Target_selectors for more information.
    """

    ENTITY = 0
    PLAYER = 1
    RANDOM = 2
    NEAREST = 3
    ALL = 4
    SELF = 5

    def __init__(self, selectorType: int):
        """Initializes a new instance of the Selector class.

        Args:
            selectorType (int): Type of the selector. Must be one of the constants in the Selector class.

        Raises:
            ValueError: Invalid selector type.
        """
        match selectorType:
            case Selector.ENTITY:
                self.selector_variable = "@e"
            case Selector.PLAYER:
                self.selector_variable = "@p"
            case Selector.RANDOM:
                self.selector_variable = "@r"
            case Selector.NEAREST:
                self.selector_variable = "@s"
            case Selector.ALL:
                self.selector_variable = "@a"
            case Selector.SELF:
                self.selector_variable = "@s"
            case _:
                raise ValueError("Invalid selector type")
        self.selector_arguments = {}

    def set_coordinate(self, x: int, y: int, z: int):
        """Sets the coordinate of the selector.

        Args:
            x (int): X position of the selector.
            y (int): Y position of the selector.
            z (int): Z position of the selector.
        """
        self.selector_arguments["x"] = x
        self.selector_arguments["y"] = y
        self.selector_arguments["z"] = z

    def set_distance(self, distance: IntRange):
        """Sets the distance of the selector.

        Args:
            distance (IntRange): Distance of the selector.
        """
        self.selector_arguments["distance"] = distance

    def set_volume(self, dx: int, dy: int, dz: int):
        """Sets the volume of the selector.

        Args:
            dx (int): The X size of the volume.
            dy (int): The Y size of the volume.
            dz (int): The Z size of the volume.
        """
        self.selector_arguments["dx"] = dx
        self.selector_arguments["dy"] = dy
        self.selector_arguments["dz"] = dz

    def set_limit(self, limit: int):
        """Sets the limit of the selector.

        Args:
            limit (int): Maximum number of entities to select.
        """
        self.selector_arguments["limit"] = limit

    def set_rotation(self, x: int | None = None, y: int | None = None):
        """Sets the rotation of the selector.

        Args:
            x (int | None, optional): The x rotation of the entity. Defaults to None.
            y (int | None, optional): The y rotation of the entity. Defaults to None.
        """
        self.selector_arguments["y_rotation"] = y
        self.selector_arguments["x_rotation"] = x

    def set_gamemode(self, gamemode: str):
        """Sets the gamemode of the selector.

        Args:
            gamemode (str): Gamemode of the entity.

        Raises:
            ValueError: Invalid gamemode.
        """
        if gamemode not in Gamemodes:
            raise ValueError("Invalid gamemode.")
        self.selector_arguments["gamemode"] = gamemode

    def set_score(self, objective: str, score: IntRange | None = None):
        """Sets the score of the selector.

        Args:
            objective (str): Objective to check.
            score (IntRange | None, optional): Value of the score. Defaults to None.
        """
        self.selector_arguments["scores"] = "{"
        if score is None:
            self.selector_arguments["scores"] += objective
        else:
            self.selector_arguments["scores"] += f"{objective}={score}"
        self.selector_arguments["scores"] += "}"

    def add_score(self, objective: str, score: IntRange | None = None):
        """Adds a score to the selector.

        Args:
            objective (str): Objective to check.
            score (IntRange | None, optional): Value of the score. Defaults to None.
        """
        if "scores" not in self.selector_arguments:
            return self.set_score(objective, score)

        self.selector_arguments["scores"] = self.selector_arguments["scores"][:-1]

        self.selector_arguments["scores"] += ","

        self.selector_arguments["scores"] += f"{objective}={score}"

        self.selector_arguments["scores"] += "}"

    def set_tag(self, tag: str):
        """Sets the tag of the selector.

        Args:
            tag (str): Tag of the entity.
        """
        self.selector_arguments["tag"] = tag

    def set_team(self, team: str):
        """Sets the team of the selector.

        Args:
            team (str): Team of the entity.
        """
        self.selector_arguments["team"] = team

    def __str__(self) -> str:
        """Returns the string representation of the selector.

        Returns:
            str: String representation of the selector.
        """
        selector = self.selector_variable
        for key, value in self.selector_arguments.items():
            selector += f"[{key}={value}]"
        return selector

    def __repr__(self) -> str:
        """Returns the string representation of the selector.

        Returns:
            str: String representation of the selector.
        """
        return f"Selector({self.selector_variable}, {self.selector_arguments})"
