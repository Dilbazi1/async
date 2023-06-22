import unittest
from server import   process_client_message

class TestServer(unittest.TestCase):
    def test_process_client_ok(self):
        self.assertEqual(process_client_message({
            'action': 'presence', 'time': 12, 'user': {'account_name': 'Guest'}}),{'response': 200})
    def test_process_client_without_action(self):
        self.assertEqual(process_client_message({
           'time': 12, 'user': {'account_name': 'Guest'}}),{'error': 'Bad Request', 'response': 400})

    def test_process_client_without_time(self):
        self.assertEqual(process_client_message({
           'action': 'presence','user': {'account_name': 'Guest'}}),{'error': 'Bad Request', 'response': 400})
    def test_process_client_without_user(self):
        self.assertEqual(process_client_message({
           'action': 'presence',   'time': 12}),{'error': 'Bad Request', 'response': 400})

    def test_process_client_without_false_accountname(self):
        self.assertEqual(process_client_message({
            'action': 'presence', 'time': 12, 'user': {'account_name': 'GUEST'}}), {'error': 'Bad Request', 'response': 400})
    def test_process_client_without_false_action(self):
        self.assertEqual(process_client_message({
            'action': 'false', 'time': 12, 'user': {'account_name': 'Guest'}}), {'error': 'Bad Request', 'response': 400})
