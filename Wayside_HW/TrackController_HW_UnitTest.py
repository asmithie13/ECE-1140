from TrackController_HW import *
from TrackController_HW_TB import *
import unittest

class TrackController_HW_UnitTest(unittest.TestCase):

    def setUp(self):
        #Set up any pre-conditions or initializations needed for your tests:
        self.TrackController_HW = TrackController_HW()
        self.TrackController_HW_TB = TrackController_HW_TB()
        self.testOne()

    def tearDown(self):
        #Clean up any resources or reset any state after each test method completes
        pass

    def testOne(self):
        #Test Case 1: Passing Speed and Authority
        testInput = ["T1", 40, 5000]
        testOut = self.TrackController_HW_TB.sendSpeedAuthority.emit(self.testInput)
        self.assertEqual(testInput, testOut)

if __name__ == '__main__':
    unittest.main()