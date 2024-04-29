import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
    
    # This test causes @quzzes_controller.py to crash on line 63
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        # with self.assertRaises(Exception):
        # Attempt to add a quiz with invalid data
        self.ctrl.add_quiz(None, None, None, None)


    # This test causes @quzzes_controller.py to crash on line 117
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        # with self.assertRaises(Exception):
        # Attempt to add a quiz with invalid data
        self.ctrl.quizzes = -1
        self.ctrl.add_question(None, None, None)


    # This test causes @quzzes_controller.py to crash on line 129
    def test_expose_failure_03(self):
        self.ctrl.clear_data()

        self.ctrl.quizzes = -1
        self.ctrl.get_question_by_id('test')
        

if __name__ == '__main__':
    unittest.main()