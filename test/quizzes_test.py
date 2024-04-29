import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_1(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.assertTrue(True, 'Example assertion.')
    
    # This test causes @quzzes_controller.py to crash on line 63
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        with self.assertRaises(Exception):
            # Attempt to add a quiz with invalid data
            self.ctrl.add_quiz(None, None, None, None)

if __name__ == '__main__':
    unittest.main()