#Fixing file hierarchy issues
import sys
import os
import re
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import unittest
from CTC.CTC_UI import *

class Test_CTC(unittest.TestCase):
    def setUp(self):
        self.CTC = CTC_UI()

    def test_throughput_calculations(self):
        testTicketSales = [[10, 20, 30, 40],[5, 5, 15, 5, 20, 0]]

        self.CTC.recieveTicketSales(testTicketSales)
        self.assertEqual(self.CTC.ThroughputGraph.heights, [100,50], 'Throughput Calculation is wrong') 


if __name__ == '__main__':
    unittest.main()