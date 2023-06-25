import unittest
from client import create_presence, process_ans


class TestClient(unittest.TestCase):
    def test_cerate_presence(self):
        test = create_presence()
        test['time'] = 12
        self.assertEqual(test, {'action': 'presence', 'time': 12, 'user': {'account_name': 'Guest'}})

    def test_create_presence_without_action(self):
        test = create_presence()
        test['time'] = 3
        self.assertNotEqual(test, {'time': 12, 'user': {'account_name': 'Guest'}})

    def test_process_ans_200(self):
        self.assertEqual(process_ans({'response': 200}), '200:OK')

    def test_process_ans_400(self):
        self.assertEqual(process_ans({'response': 400, 'error': 'Bad Request'}), '400 :Bad Request')

    def test_process_ans_error(self):
        self.assertRaises(ValueError, process_ans, {'error': 'Bad Request'})
