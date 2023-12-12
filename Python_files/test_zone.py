class BookReview:

    def __init__(self, book_title):
        self.book_title = book_title
        self.reviews = []
    
    def add_review(self, reviewer_name, review):
        self.reviews.append((reviewer_name, review))
        print(f"These are the reviews: {self.reviews}")
    
    def get_all_reviews(self):
        return self.reviews
    
    def average_review_length(self):
        sum_lenght = 0
        sum_loop = 0
        for single_review in self.reviews:
            string_without_period = single_review[1].replace('.', '')
            length = len(string_without_period)
            sum_loop += 1
            print(f"this is the sum of the previous lenght and the actual: {sum_lenght} + {length}")
            sum_lenght =  sum_lenght + length
            print(f"this is loop counter: {sum_loop}")
            print(f"this is lenght: {sum_lenght}")
        print (f"this should be the average: {sum_lenght / sum_loop}")
        return sum_lenght / sum_loop

my_object = BookReview("Alicia")
my_object.add_review("Alice", "Great book.")
my_object.add_review("Bob", "Informative.")
my_object.average_review_length()
