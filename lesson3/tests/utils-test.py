import os
import sys
import json
import time
import unittest
from unittest.mock import patch

sys.path.append(os.getcwd())

from common.variables import ERROR, ENCODING, MAX_PACKAGE_LENGTH

import unittest

from common.utils import get_message, send_message
class TestSocket:
    def __init__(self, message):
        self.encoded_message = json.dumps(message).encode(ENCODING)

    def recv(self, package_length=MAX_PACKAGE_LENGTH):
        return self.encoded_message

    def send(self, message):
        self.send = json.loads(message.decode(ENCODING))

class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.time = 12
        self.message = {"action": "msg", "time": self.time}

        self.test_sock = TestSocket(self.message)






    def test_get_message(self):
        test_sock = TestSocket(self.message)
        message = get_message(test_sock)
        self.assertEqual(message, self.message)

    def test_send_message(self):
        send_message(self.test_sock, self.message)
        self.assertEqual(self.test_sock.send, self.message)


if __name__ == "__main__":
    unittest.main()
