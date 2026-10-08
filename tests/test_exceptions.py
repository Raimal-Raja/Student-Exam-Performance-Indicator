import sys
import unittest

from src.exception import CustomException


class ExceptionTests(unittest.TestCase):
    def test_low_score_message_without_active_exception(self):
        error = CustomException('No best model found')
        self.assertIn('No best model found', str(error))
        self.assertIn('<no active traceback>', str(error))

    def test_wrapped_exception_preserves_traceback_location(self):
        try:
            raise ValueError('invalid input')
        except ValueError as cause:
            error = CustomException(cause, sys)
        self.assertIn(__file__, str(error))
        self.assertIn('invalid input', str(error))


if __name__ == '__main__':
    unittest.main()
