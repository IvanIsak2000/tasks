import unittest 

class Test(unittest.TestCase):

    def test_numbers_is_equals(self):
        self.assertEqual(1,1)
    
    def test_lists_is_equals(self):
        self.assertEqual([1,2,3,4,5],[1,2,3,4,5])

    def test_number_is_not_equals(self):
        self.assertNotEqual(1,2)

if __name__ == '__main__':
    unittest.main()