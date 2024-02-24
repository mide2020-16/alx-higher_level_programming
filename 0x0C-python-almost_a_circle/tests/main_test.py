import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_base_instance_creation(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base(10)
        self.assertEqual(obj2.id, 10)

    def test_base_to_json_string(self):
        dictionaries = [{'id': 1, 'name': 'Object 1'}, {'id': 2, 'name': 'Object 2'}]
        json_string = Base.to_json_string(dictionaries)
        expected_json_string = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        self.assertEqual(json_string, expected_json_string)

    def test_base_from_json_string(self):
        json_string = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        dictionaries = Base.from_json_string(json_string)
        expected_dictionaries = [{'id': 1, 'name': 'Object 1'}, {'id': 2, 'name': 'Object 2'}]
        self.assertEqual(dictionaries, expected_dictionaries)

    def test_base_create_instance_from_dictionary(self):
        dictionary = {'id': 1, 'name': 'Object 1'}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj, 'Object 1')

    def test_base_load_from_file(self):
# Test loading instances from file
# Note: Make sure to create a test file 'Base.json' with appropriate content for this test
        instances = Base.load_from_file()
        self.assertIsInstance(instances, list)

class TestRectangle(unittest.TestCase):
    def test_rectangle_instance_creation(self):
        obj1 = Rectangle(2, 4)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj1.width, 2)
        self.assertEqual(obj1.height, 4)

        obj2 = Rectangle(3, 5, 1, 1, 10)
        self.assertEqual(obj2.id, 10)
        self.assertEqual(obj2.width, 3)
        self.assertEqual(obj2.height, 5)
        self.assertEqual(obj2.x, 1)
        self.assertEqual(obj2.y, 1)

# Add more test cases for Rectangle class as needed

class TestSquare(unittest.TestCase):
    def test_square_instance_creation(self):
        obj1 = Square(4)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj1.size, 4)

        obj2 = Square(5, 1, 1, 10)
        self.assertEqual(obj2.id, 10)
        self.assertEqual(obj2.size, 5)
        self.assertEqual(obj2.x, 1)
        self.assertEqual(obj2.y, 1)

# Add more test cases for Square class as needed

if __name__ == '__main__':
    unittest.main()
