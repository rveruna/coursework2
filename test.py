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
        self.assertIn(b'You were just logged in', response.data)

    #ensure that login behaves INcorrectly given the correct credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid Credentials. Please try again.', response.data)

    #ensure that logout page loads correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)

    #ensure main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first.' in response.data)

    #ensure that post appear on post page
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hello from', response.data)



if __name__ == '__main__':
    unittest.main()
