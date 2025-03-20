import unittest
from exercises.theLifeOfPi import theLifeOfPi_tupel

class MyTestCase_TheLifeOfPi(unittest.TestCase):
    def test_stringequality_tupel(self):
        restupel_nach_angabe = (
            "3.141593!",
            "    3.141593!",
            "     3!",
            "3.14159265359!",
            "00000003.141593!",
            "+00000000003.14!"
        )
        self.assertEqual(theLifeOfPi_tupel(), restupel_nach_angabe)


if __name__ == '__main__':
    unittest.main()
