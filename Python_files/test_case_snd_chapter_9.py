import unittest
from snd_chapter_9 import FitnessClassScheduler, BookReview
 
class TestFitnessClassScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = FitnessClassScheduler("Yoga")
 
    def test_schedule_session(self):
        self.scheduler.schedule_session("2023-12-10", "John")
        self.assertIn("2023-12-10", self.scheduler.scheduled_sessions)
        self.assertEqual(self.scheduler.scheduled_sessions["2023-12-10"], "John")
 
    def test_cancel_session(self):
        self.scheduler.schedule_session("2023-12-11", "Jane")
        self.scheduler.cancel_session("2023-12-11")
        self.assertNotIn("2023-12-11", self.scheduler.scheduled_sessions)
 
    def test_list_sessions(self):
        self.scheduler.schedule_session("2023-12-10", "John")
        expected_sessions = ["2023-12-10: John"]
        self.assertEqual(self.scheduler.list_sessions(), expected_sessions)
 
if __name__ == '__main__':
    unittest.main()

class TestBookReview(unittest.TestCase):
    def setUp(self):
        self.book = BookReview("Python Programming")
 
    def test_add_review(self):
        self.book.add_review("Alice", "Great book for beginners.")
        self.assertIn(("Alice", "Great book for beginners."), self.book.reviews)
 
    def test_get_all_reviews(self):
        self.book.add_review("Bob", "Very informative and well-written.")
        expected_reviews = [("Bob", "Very informative and well-written.")]
        self.assertEqual(self.book.get_all_reviews(), expected_reviews)
 
    def test_average_review_length(self):
        self.book.add_review("Alice", "Great book.")
        self.book.add_review("Bob", "Informative.")
        expected_average = (10 + 11) / 2
        self.assertEqual(self.book.average_review_length(), expected_average)
 
if __name__ == '__main__':
    unittest.main()