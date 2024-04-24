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
    
    
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        with self.assertRaises(Exception):
            # Attempt to add a quiz with invalid data
            self.ctrl.add_quiz(None, None, None)
            
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        # Add a quiz for control
        self.ctrl.add_quiz("quiz1", "category1", "difficulty1", "2022-12-31")
        # Attempt to retrieve a quiz that doesn't exist
        result = self.ctrl.get_quiz_by_id("non_existent_quiz_id")
        # Assert that the result is None
        self.assertIsNone(result, "Quiz found with id non_existent_quiz_id")

    def test_expose_failure_03(self):
        self.ctrl.clear_data()
        with self.assertRaises(Exception):
            # Attempt to delete a quiz that doesn't exist
            self.ctrl.delete_quiz("non_existent_quiz_id")

if __name__ == '__main__':
    unittest.main()