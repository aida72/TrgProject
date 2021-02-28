import unittest
from hello_world import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config["SERVER_NAME"] = 'localhost:8087'
        self.app = app.test_client()
    def test_hello(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status, '200 OK')
        self.assertEqual(resp.data, b'Hello World!')
if __name__ == '__main__':
    unittest.main()