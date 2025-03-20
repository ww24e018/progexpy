import unittest

from exercises.TimeCalculator import TimeCalculator_dict, TimeCalculator_tupel

class MyTestCaseForTimeCalculator(unittest.TestCase):
    def test_angabe_dictreturn(self):
        tm = TimeCalculator_dict(3452347890)
        self.assertEqual(tm['ms'],890)
        self.assertEqual(tm['seconds'],7)
        self.assertEqual(tm['minutes'],59)
        self.assertEqual(tm['hours'],22)
        self.assertEqual(tm['days'],39)
        self.assertEqual(tm['duration_total'],3452347890)
    def test_angabe_tupelreturn(self):
        tm = TimeCalculator_tupel(3452347890)
        self.assertEqual(tm, (3452347890,39,22,59,7,890))
    def test_tupelZero(self):
        tm = TimeCalculator_tupel(0)
        self.assertEqual(tm, (0,0,0,0,0,0))

if __name__ == '__main__':
    unittest.main()
