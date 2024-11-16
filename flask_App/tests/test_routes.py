import unittest
from flask_app.app import app  # importing the app

# test case to check route behavior
class TestRoutes(unittest.TestCase):
    # set up a test client for the app
    def setUp(self):
        self.app = app.test_client()

    # test if a post request to a get-only route returns a 405 status code
    def test_route_method_not_allowed(self):
        response = self.app.post('/home')  # assuming /home is a get-only route
        self.assertEqual(response.status_code, 405)  # assert that method not allowed is returned

# run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()