#!/usr/bin/python3
"""unit testing done using unittest module"""
import unittest
Base = __import__('base').Base


class testBase(unittest.TestCase):
    """test cases for base class"""
    def test_id(self):
        """test the initialization of base class with id"""
        base_obj = Base()
        self.assertEqual(base_obj.id, 1)
        base_obj = Base()
        base_obj = Base()
        self.assertEqual(base_obj.id, 3)
        base_obj = Base(4)
        self.assertEqual(base_obj.id, 4)
        base_obj = Base(None)
        self.assertEqual(base_obj.id, 4)

    def test_to_json_string(self):
        """testing to_json_string method"""
        dic_list = [{"size": 10, "x": 2, "y": 4, "id": 3}]
        j_string = Base.to_json_string(dic_list)
        self.assertEqual(j_string, '[{"size": 10, "x": 2, "y": 4, "id": 3}]')
        dic_list = []
        j_string = Base.to_json_string(dic_list)
        self.assertEqual(j_string, "[]")
        dic_list = None
        j_string = Base.to_json_string(dic_list)
        self.assertEqual(j_string, "[]")

if __name__ == '__main__':
    unittest.main()
