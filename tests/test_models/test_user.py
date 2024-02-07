#!/usr/bin/python3

class TestUser(unittest.TestCase):

    def setUp(self):
        self.my_user = User()

    def test_attributes_initialization(self):
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "")
        self.assertEqual(self.my_user.first_name, "")
        self.assertEqual(self.my_user.last_name, "")

if __name__ == '__main__':
    unittest.main()
