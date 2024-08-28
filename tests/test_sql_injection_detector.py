import unittest
from sql_injection_detector.app import app

class SQLInjectionDetectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
    

    def test_valid_query(self):
        response = self.client.post('/test', data={'query': 'SELECT * FROM users WHERE id=1'})
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_in_query_param(self):
        response = self.client.get('/test', query_string={'param': '1 OR 1=1'})
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_in_form_data(self):
        response = self.client.post('/test', data={'param': '1 OR 1=1'})
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_in_headers(self):
        response = self.client.post('/test', headers={'Injection-Test': '1 OR 1=1'})
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_in_raw_body(self):
        response = self.client.post('/test', data='SELECT * FROM users WHERE id=1; DROP TABLE users;')
        self.assertEqual(response.status_code, 403)
        
    def test_no_injection_in_query(self):
        response = self.client.post('/test', data={'query': 'SELECT id FROM users WHERE name="John"'})
        self.assertEqual(response.status_code, 403)  

    def test_injection_with_comments_in_query(self):
        response = self.client.post('/test', data={'query': 'SELECT * FROM users --'})
        self.assertEqual(response.status_code, 403)

    def test_injection_with_case_variation(self):
        response = self.client.post('/test', data={'query': 'SeLeCt * fRoM users WHERE id=1'})
        self.assertEqual(response.status_code, 403)

    def test_injection_with_malformed_patterns(self):
        response = self.client.post('/test', data={'param': '1 AND (1=1 OR 1=2) AND 1=1'})
        self.assertEqual(response.status_code, 403)

    def test_valid_input_with_escaped_characters(self):
        response = self.client.post('/test', data={'query': 'SELECT * FROM users WHERE name=\'O\'Reilly\''})
        self.assertEqual(response.status_code, 403)

    def test_injection_with_hex_values(self):
        response = self.client.post('/test', data={'query': 'SELECT * FROM users WHERE id = 0x1'})
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_with_multiple_injections(self):
        response = self.client.post('/test', data={'param': '1 OR 1=1; DROP TABLE users; --'})
        self.assertEqual(response.status_code, 403)

    def test_injection_with_subqueries(self):
        response = self.client.post('/test', data={'query': 'SELECT * FROM users WHERE id IN (SELECT id FROM admins)'})
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
