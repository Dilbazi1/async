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


class TestUtils(unittest.TestCase):
    def test_process_ans_error(self):
        sock={'action': 'presence', 'time': 1687109514.307525, 'user': {'account_name': 'Guest'}}

        self.assertRaises(ValueError, get_message(socket),)


if __name__ == "__main__":
    unittest.main()
