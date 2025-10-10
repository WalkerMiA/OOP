class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.booksBorrowed = []
    def add_user(self):
        self.userID = input("Enter user ID: ")
        self.userName = input("Enter user name: ")
    def add_book(self, bbook):
        self.booksBorrowed.append(bbook)
    def display_books(self):
        print("UserID:", self.userID)
        print("UserName:", self.userName)
        for x in self.booksBorrowed:
            print("Books Borrowed:", x.title)

class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.bookID = ""
    def create_book(self):
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")
        self.bookID = input("Enter book ID: ")

user1 = User()
user1.add_user()

user2 = User()
user2.add_user()

book1 = Book()
book1.create_book()
book2 = Book()
book2.create_book()
book3 = Book()
book3.create_book()
book4 = Book()
book4.create_book()
book5 = Book()
book5.create_book()

user1.add_book(book1)
user1.add_book(book3)
user1.add_book(book5)

user2.add_book(book2)
user2.add_book(book4)

user1.display_books()
user2.display_books()
