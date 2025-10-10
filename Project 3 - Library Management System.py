class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email_id = ""
        self.booksBorrowed = []
    def add_user(self):
        self.userID = input("Enter user ID: ")
        self.userName = input("Enter user name: ")
        self.password = input("Enter your password:")
        self.address = input("Enter your address:")
        self.phone = input("Enter your phone number:")
        self.email_id = input("Enter your email:")
    def borrow_book(self, bbook):
        self.booksBorrowed.append(bbook)
    def display_borrowed_books(self):
        print("UserID:", self.userID)
        print("UserName:", self.userName)
        for x in self.booksBorrowed:
            print("Books Borrowed:", x.title)
    def display_user(self):
        user = input("Enter user ID:")
        print(user)

class Book:
    def __init__(self):
        self.book_id = ""
        self.book_name = ""
        self.author_id = ""
        self.publisher = ""
        self.year_published = ""
    def add_book(self):
        self.book_id = input("Enter book ID: ")
        self.book_name = input("Enter title: ")
        self.author_id = input("Enter author ID: ")
        self.publisher = input("Enter the publisher:")
        self.year_published = input("Enter the year published:")

class Author:
    def __init__(self):
        self.author_name = ""
        self.author_id = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""
    def add_author(self):
        self.author_name = input("Enter author name:")
        self.author_id = input("Enter author ID:")
        self.affiliation = input("Enter author's affiliation:")
        self.country = input("Enter author's country:")
        self.phone = input("Enter the author's phone number:")
        self.email_id = input("Enter the author's email:")

user1 = User()
user1.add_user()
user1.display_user()