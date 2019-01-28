import unittest

def multiply(a, b):
    return a * b
	
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_case1(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_case2(self):
        self.assertEqual( multiply('a',3), 'aaa')

    def test_case3(self):
        self.assertTrue( 5 < 10, True )

    def test_case4(self):
        self.assertIn( 5, list(range(1,6)))

    def test_case5(self):
        self.assertNotIn( 50, list(range(1,6)))		
		
if __name__ == '__main__':
    unittest.main()
    
