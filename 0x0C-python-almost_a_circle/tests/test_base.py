import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_assignment_auto(self):
        """Test automatic id assignment."""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_assignment_manual(self):
        """Test manual id assignment."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_id_unique(self):
        """Test that id is unique."""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b4.id)
        self.assertNotEqual(b1.id, b4.id)

    def test_id_none(self):
        """Test that passing None is like passing no argument."""
        Base._Base__nb_objects = 0
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()
