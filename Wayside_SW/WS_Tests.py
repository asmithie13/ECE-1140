import unittest
from unittest.mock import Mock

class TestUpdateBlocks(unittest.TestCase):
    def setUp(self):
        self.obj.currentBlocks = [Mock(), Mock()]
        self.obj.occupiedBlocks = [Mock()]

class TestBlockClosures(unittest.TestCase):
    def setUp(self):
        self.obj.currentBlocks = [Mock(), Mock()]
        self.obj.allGreenBlocks = [Mock(), Mock()]
        self.obj.allRedBlocks = [Mock(), Mock()]
        self.obj.occupiedBlocks = [Mock()]

    def test_blockClosures_green_maintenance(self):
        closed_blocks = 2
        for block in closed_blocks:
            block.lineColor = "Green"
            block.maintenance = True
        self.obj.blockClosures(closed_blocks)

    def test_blockClosures_red_no_maintenance(self):
        closed_blocks = 2
        for block in closed_blocks:
            block.lineColor = "Red"
            block.maintenance = False
        self.obj.blockClosures(closed_blocks)



if __name__ == '__main__':
    unittest.main()
