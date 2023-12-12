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

"""
Question 4: Book Review System
Description:
Create a class called BookReview. It should have the following 
attributes and methods:

Attributes: book_title (string), reviews (list of tuples, 
each tuple containing a reviewer’s name and their review 
as a string).

Methods:
add_review(reviewer_name, review): Adds a new review to the book.
get_all_reviews(): Returns a list of all reviews for the book.
average_review_length(): Returns the average length of all reviews.
"""

class BookReview:

    def __init__(self, book_title):
        self.book_title = book_title
        self.reviews = []
    
    def add_review(self, reviewer_name, review):
        self.reviews.append((reviewer_name, review))
    
    def get_all_reviews(self):
        return self.reviews
    
    def average_review_length(self):
        sum_lenght = 0
        sum_loop = 0
        for single_review in self.reviews:
            string_without_period = single_review[1].replace('.', '')
            length = len(string_without_period)
            sum_loop += 1
            sum_lenght += length
        return sum_lenght / sum_loop
