import unittest

from minegive.modules.Gamemodes import Gamemodes


class TestGamemodes(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(Gamemodes.SPECTATOR, "spectator")
        self.assertEqual(Gamemodes.SURVIVAL, "survival")
        self.assertEqual(Gamemodes.CREATIVE, "creative")
        self.assertEqual(Gamemodes.ADVENTURE, "adventure")


if __name__ == "__main__":
    unittest.main()
