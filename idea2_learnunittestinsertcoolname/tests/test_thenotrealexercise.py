import unittest

from exercises.NotARealExercise import MyFirstFunction

class MyTestCaseForNotARealExercise(unittest.TestCase):
    """This file is mainly from pycharm 2024.3.5 CE; I changed the class name though"""
    def test_something(self):
        self.assertEqual(MyFirstFunction(), 'Returns A String')  # add assertion here


if __name__ == '__main__':
    unittest.main()
