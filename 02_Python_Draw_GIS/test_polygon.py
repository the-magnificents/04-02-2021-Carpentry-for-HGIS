import unittest
from polygon import *
import turtle


# Setup the test calss and inherit the mehtods
class TestPolygon(unittest.TestCase):
    
    def test_sort_points(self):
        self.assertEqual(sort_points([[10,50],[50,10],[30,20]]),
                                        [[50,10],[30,20],[10,50]])
        self.assertEqual(sort_points([[10,50],[30,20],[50,10]]),
                                        [[50,10],[30,20],[10,50]])
        
    def test_get_angle(self):
        self.assertEqual(get_angle([50,10]), 11.309932474020215)
        # Coordinates in third quadrant
        self.assertEqual(round(get_angle([-158,-80])),297)
        # Angle is bigger than 360
        self.assertEqual(round(get_angle([221,-10])),-3)
        # Angle bigger than 360
        self.assertEqual(round(get_angle([121.66, -260.0])),-65)
    
    def test_sort_item(self):
        self.assertEqual(sort_item(2,[[20,30],[10,50],[50,10]]),[[50,10],[20,30],[10,50]])

if __name__ == '__main__':
    # Run the whole test
    unittest.main()