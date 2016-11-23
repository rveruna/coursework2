from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #ensure that flask is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    #ensure that login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
        '/login', 
        data=dict(username="admin", password="admin"),
        follow_redirects=True
        )
        self.assertIn(b'You were just logged in' in response.data)


if __name__ == '__main__':
    unittest.main()
