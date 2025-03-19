import unittest

"""
this cursed piece of code comes courtesy of chatgpt with 
a modification implied by a piece of stackoverflow.

I could *not* reproduce the syntax by looking at the examples in the python doc
Seems underdocumented. It *seems* to work though. Perhaps. Maybe. I don't trust it.
"""
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.discover("tests"))