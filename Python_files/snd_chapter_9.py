"""
Question 5: Fitness Class Scheduler
Description:
Create a class called FitnessClassScheduler. 
It should have the following attributes and methods:

Attributes: class_name (string), 
scheduled_sessions (dictionary with date strings as keys and instructor names as values).

Methods:
schedule_session(date, instructor_name): Schedules a new fitness class session.
cancel_session(date): Cancels a scheduled session.
list_sessions(): Returns a list of all scheduled sessions in the format 
“Date: Instructor”.
"""

class FitnessClassScheduler:

    def __init__(self, class_name):
        self.class_name = class_name
        self.scheduled_sessions = {}
    
    def schedule_session(self, date, instructor_name):
        self.scheduled_sessions[date] = instructor_name
    
    def cancel_session(self, date):
        del self.scheduled_sessions[date]
    
    def list_sessions(self):
        list1 = []
        for date, instructor in self.scheduled_sessions.items():
            list1.append(f"{date}: {instructor}")
        return list1

