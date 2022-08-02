#!/usr/bin/env python3
import unittest
import main
import random
ran = random.randrange(1000)
class TestHelloDevops(unittest.TestCase):

    def setUp(self):
        main.web.testing = True
        self.app = main.web.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("What would you like to do:", 'utf-8'), rv.data)
   
    def test_get(self):
        rv = self.app.get('/get')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("GigabitEthernet", 'utf-8'), rv.data)
   
    def test_add(self):
        ran = str(123)
        rv = self.app.get(f'/add/{ran}/desk/10.10.10.10/255.255.255.0')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"Loopback{ran}", 'utf-8'), rv.data)

    def test_del(self):
        ran = str(123)
        rv = self.app.get(f'/add/{ran}/desk/10.10.10.10/255.255.255.0')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"Loopback{ran}", 'utf-8'), rv.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
