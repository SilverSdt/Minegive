import unittest

from minegive.modules.ArgumentTypes import IntRange
from minegive.modules.Gamemodes import Gamemodes
from minegive.modules.Selector import Selector


class TestSelector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Selector(10)  # Invalid selector type
        selector = Selector(Selector.PLAYER)
        self.assertEqual(str(selector), "@p")

    def test_set_coordinate(self):
        selector = Selector(Selector.PLAYER)
        selector.set_coordinate(1, 2, 3)
        self.assertEqual(str(selector), "@p[x=1][y=2][z=3]")

    def test_set_distance(self):
        selector = Selector(Selector.PLAYER)
        selector.set_distance(IntRange(1, 10))
        self.assertEqual(str(selector), "@p[distance=1..10]")

    def test_set_volume(self):
        selector = Selector(Selector.PLAYER)
        selector.set_volume(1, 2, 3)
        self.assertEqual(str(selector), "@p[dx=1][dy=2][dz=3]")

    def test_set_limit(self):
        selector = Selector(Selector.PLAYER)
        selector.set_limit(5)
        self.assertEqual(str(selector), "@p[limit=5]")

    def test_set_rotation(self):
        selector = Selector(Selector.PLAYER)
        selector.set_rotation(90, 180)
        self.assertEqual(str(selector), "@p[y_rotation=180][x_rotation=90]")

    def test_set_gamemode(self):
        selector = Selector(Selector.PLAYER)
        selector.set_gamemode(Gamemodes.SURVIVAL)
        self.assertEqual(str(selector), "@p[gamemode=survival]")

    def test_set_score(self):
        selector = Selector(Selector.PLAYER)
        selector.set_score("objective", IntRange(1, 10))
        self.assertEqual(str(selector), "@p[scores={objective=1..10}]")

    def test_add_score(self):
        selector = Selector(Selector.PLAYER)
        selector.add_score("objective", IntRange(1, 10))
        self.assertEqual(str(selector), "@p[scores={objective=1..10}]")

    def test_set_tag(self):
        selector = Selector(Selector.PLAYER)
        selector.set_tag("tag")
        self.assertEqual(str(selector), "@p[tag=tag]")

    def test_set_team(self):
        selector = Selector(Selector.PLAYER)
        selector.set_team("team")
        self.assertEqual(str(selector), "@p[team=team]")


if __name__ == "__main__":
    unittest.main()
