
import unittest
 

class TestUM(unittest.TestCase):
 

 
    def test_numbers(self):
        self.assertEqual( 12, 121)
 
    def test_strings(self):
        self.assertEqual( "perl" , 'perl'.lower())
 
 
 
if __name__ == '__main__':
    unittest.main()


#setup
#teardown
