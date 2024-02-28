#!/usr/bin/python3
"""A test script utilizing unittest module to test the feature of a class"""
import unittest
Square = __import__('square').Square


class Test_Square(unittest.TestCase):
    """tests the features of Square class"""
    def test_initialization(self):
        """testing the initialisation of the class"""
        s = Square(10, 1, 3, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 7)
        s2 = Square(10, 2, 2)
        s3 = Square(5, 3)
        s4 = Square(4)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.size, 5)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s4.size, 4)
        with self.assertRaises(TypeError):
            s = Square(0)
        with self.assertRaises(TypeError):
            s = Square(-0)
        with self.assertRaises(TypeError):
            s = Square(5, -1)
        with self. assertRaises(TypeError):
            s = Square(6, 3, -0)
        with self.assertRaises(ValueError):
            s = Square(0, 1, 3, 7)
        with self.assertRaises(ValueError):
            s = Square(-1, 2, 3, 7)
        with self.assertRaises(ValueError):
            s = Square(1, -2, 4, 5)
        with self.assertRaises(ValueError):
            s = Square(1, 1, -2, 4)
        with self.assertRaises(ValueError):
            s = Square(0, 4)

    def test_properties(self):
        """test getter and setter methods"""
        s = Square(10, 1, 3, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 7)
        s = Square(11, 2, 5)
        self.assertEqual(s.size, 11)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 5)

    def test_update_square(self):
        """test update method"""
        s = Square(1, 2, 3, 4)
        s.update(2, 4, 6, 8)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 2)
        s.update(10, 2, 4,)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.id, 10)
        s.update(50, 2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.id, 50)
        s.update(2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.x, 4)
        s.update()
        self.assertEqual(s.size, 2)

    def test2_update_square(self):
        """testing the update method with keyword arguments"""
        s = Square(1, 2, 3, 4)
        s.update(size=10, x=2, y=3, id=4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        s.update(size=5, x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 4)
        s.update(x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test3_update_square(self):
        """testing the update method with none int values"""
        s = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s.update("2", 4, 5)
            s.update(True, 5, 5)
            s.update(2, 4, 4.78)
        with self.assertRaises(ValueError):
            s.update(0, 2, 4)
            s.update(-2, 6)
            s.update(6, -1)
            s.update(4, 6, -8)

    def test4_str_(self):
        """testing for __str__ method"""
        s = Square(5, 3, 3, 5)
        self.assertEqual(s.__str__(), "[Square] (5) 3/3 - 5")

    def test_to_dictionary(self):
        """testing the to_dictionary method in Square class"""
        s = Square(10, 2, 2, 3)
        dic = {"id": 3, "size": 10, "x": 2, "y": 2}
        self.assertEqual(s.to_dictionary(), dic)

    def test_create(self):
        """testing create method"""
        s = Square(2, 3, 4, 6)
        dic = s.to_dictionary()
        new_obj = s.create(**dic)
        self.assertTrue(isinstance(new_obj, Square))
        s1 = Square(2, 3, 4)
        dic = s1.to_dictionary()
        new_obj = s1.create(**dic)
        self.assertIsInstance(new_obj, Square)
        s2 = Square(2, 3)
        dic = s2.to_dictionary()
        new_obj = s2.create(**dic)
        self.assertIsInstance(new_obj, Square)

if __name__ == '__main__':
    unittest.main()
