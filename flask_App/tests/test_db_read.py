import unittest
from flask_app.app import db  # importing the db instance

# test case to check database connection
class TestDBRead(unittest.TestCase):
    # test if the database responds to a ping command
    def test_ping_database(self):
        self.assertTrue(db.command("ping"))  # assert that the ping command returns true

# run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()