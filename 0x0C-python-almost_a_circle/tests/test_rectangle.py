import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        """Test initialization of Rectangle"""
        r = Rectangle(10, 15, 5, 5, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 1)

    def test_width_attr(self):
        """Test getter and setter for width."""
        r = Rectangle(10, 20)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_height_attr(self):
        """Test getter and setter for height."""
        r = Rectangle(10, 20)
        r.height = 25
        self.assertEqual(r.height, 25)

    def test_x_attr(self):
        """Test getter and setter for x."""
        r = Rectangle(10, 20, 5)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_y_attr(self):
        """Test getter and setter for y."""
        r = Rectangle(10, 20, 5, 5)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_negative_width(self):
        """Test that setting a negative width raises an error."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_neg_height(self):
        """Test that setting a negative height raises an error."""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -20

    def test_neg_x(self):
        """Test that setting a negative x raises an error."""
        r = Rectangle(10, 20, 5)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_neg_y(self):
        """Test that setting a negative y raises an error."""
        r = Rectangle(10, 20, 5, 5)
        with self.assertRaises(ValueError):
            r.y = -5

if __name__ == '__main__':
    unittest.main()
