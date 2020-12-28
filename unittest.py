import unittest
#import code
import actualcode as freshworks
class TestMethod(unittest.TestCase):
   # f=freshworks()
    def test_create(self):
        self.assertEqual(freshworks.flag(),1)
    def test_read(self):
        self.assertEqual(freshworks.r(),1)
    def test_modify(self):
        self.assertEqual(freshworks.m(),1)
    def test_delete(self):
        self.assertEqual(freshworks.dele(),1)
    
if __name__ == '__main__':
    unittest.main()

