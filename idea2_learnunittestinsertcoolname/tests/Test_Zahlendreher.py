import unittest
from exercises.Zahlendreher import Zahlendreher

class MyTestCase_Zahlendreher(unittest.TestCase):
    def test_angabe(self):
        self.assertEqual(Zahlendreher(123), "321")
        self.assertEqual(Zahlendreher(12), "210")
        self.assertEqual(Zahlendreher(1), "100")
        self.assertEqual(Zahlendreher(120), "021")
        self.assertEqual(Zahlendreher(0), "000")


if __name__ == '__main__':
    unittest.main()
