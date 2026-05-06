""""Q9. Design a LibraryMember class that:
•	Tracks total active members.
•	Each member has a name and books_borrowed count.
•	Has a function to borrow books, with borrowing limit common to all.
•	Allows updating borrowing limit globally.
•	Has a static function to check if book title is valid (non-empty string, reasonable length).
Demonstrate:
1.	Borrowing books for multiple users.
2.	Changing borrowing limits.
3.	Validating book titles before borrowing.
"""
class LibraryMember:
    total_active_members=0
    borrowing_limit=5
    def __init__(self,name,books_borrowed_count):
        self.name=name
        self.books_borrowed_count=books_borrowed_count
        LibraryMember.total_active_members+=1
    def borrow_books(self,books_to_be_borrowed):
        if self.books_borrowed_count<LibraryMember.borrowing_limit:
            self.books_borrowed_count+=books_to_be_borrowed
            return self.books_borrowed_count
        else:
            return f"You cannot borrow more books"
    @classmethod
    def update_borrowing_limit(cls,new_limit):
        cls.borrowing_limit=new_limit
    @staticmethod
    def valid(book_name):
        if len(book_name)>=4:
            return True
        return False

user1=LibraryMember("Swadeep",2)
user2=LibraryMember("Deekshith",1)
user3=LibraryMember("Saikrishna",4)
user1.borrow_books(3)#borrowing 3 more books
user2.borrow_books(2)#borrowing 2 more books
print(user1.borrow_books(3)) #if i try to take more books than the limit it will give a message
print("Books borrowed by user1:",user1.books_borrowed_count) #printing the books user1 borrowed
print("Books borrowed by user2:",user2.books_borrowed_count) #printing the books borrowed by user2
LibraryMember.update_borrowing_limit(8)
print(LibraryMember.borrowing_limit)