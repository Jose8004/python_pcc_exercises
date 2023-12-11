import unittest
from snd_chapter_9 import FitnessClassScheduler
 
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