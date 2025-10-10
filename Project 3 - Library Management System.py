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
            print("Books Borrowed:", x.book_name)

    def display_user(self):
        print("UserID:", self.userID)
        print("UserName:", self.userName)
        print("UserAddress:", self.address)
        print("UserPhone:", self.phone)
        print("UserEmailID:", self.email_id)
        for x in self.booksBorrowed:
            print("Books Borrowed:", x.book_name)

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
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Book Name:", self.book_name)
        print("AuthorID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year Published:", self.year_published)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email_id = ""
    def add_author(self):
        self.author_id = input("Enter author ID:")
        self.author_name = input("Enter author name:")
        self.affiliation = input("Enter author's affiliation:")
        self.country = input("Enter author's country:")
        self.phone = input("Enter the author's phone number:")
        self.email_id = input("Enter the author's email:")
    def display_author(self):
        print("AuthorID:", self.author_id)
        print("AuthorName:", self.author_name)
        print("AuthorAffiliation:", self.affiliation)
        print("AuthorCountry:", self.country)
        print("AuthorPhone:", self.phone)
        print("AuthorEmailID:", self.email_id)

users = {}
authors = {}
books = {}

def create_new_user():
    new_user = User()
    new_user.add_user()
    if new_user.userID in users:
        print("User already exists")
    else:
        users[new_user.userID] = new_user
        print("New user created")

def edit_user():
    user_id = input("Enter user ID to edit: ")
    if user_id not in users:
        print("User does not exist")
        return
    user = users[user_id]
    new_name = input("Enter new name")
    new_password = input("Enter new password")
    new_address = input("Enter new address")
    new_phone = input("Enter new phone number")
    new_email_id = input("Enter new email ID")

    if new_name:
        user.userName = new_name
    if new_password:
        user.password = new_password
    if new_address:
        user.address = new_address
    if new_phone:
        user.phone = new_phone
    if new_email_id:
        user.email_id = new_email_id
    print("User updated")

def display_all_users():
    for user in users.values():
        user.display_user()

def create_new_book():
    new_book = Book()
    new_book.add_book()
    if new_book.book_id in books:
        print("Book already exists")
    else:
        books[new_book.book_id] = new_book
        print("New book created")

def edit_book():
    book_id = input("Enter book ID to edit: ")
    if book_id not in books:
        print("Book does not exist")
        return

    book = books[book_id]
    new_book_name = input("Enter new book name:")
    new_book_author_id = input("Enter new author ID:")
    new_book_publisher = input("Enter new publisher:")
    new_book_year_published = input("Enter new year published:")
    if new_book_name:
        book.book_name = new_book_name
    if new_book_author_id:
        book.author_id = new_book_author_id
    if new_book_publisher:
        book.publisher = new_book_publisher
    if new_book_year_published:
        book.year_published = new_book_year_published
    print("Book updated")


def display_all_books():
    for book in books.values():
        book.display_book()

def user_borrows_books():
    user_id = input("Enter user ID: ")
    if user_id not in users:
        print("User does not exist")
        return

    user = users[user_id]
    number_of_borrowed = int(input("Enter number of books borrowed:"))
    for x in range(number_of_borrowed):
        book_id = input("Enter book ID: ")
        if book_id not in books:
            print("Book does not exist")
            return
        else:
            book = books[book_id]
            user.borrow_book(book)
            print("Book borrowed:", book.book_name)

def create_new_author():
    new_author = Author()
    new_author.add_author()
    if new_author.author_id in authors:
        print("Author already exists")
    else:
        authors[new_author.author_id] = new_author
        print("New author created")

def edit_author():
    author_id = input("Enter author ID: ")
    if author_id not in authors:
        print("Author does not exist")
        return
    author = authors[author_id]
    new_author_name = input("Enter new author's name:")
    new_author_affiliation = input("Enter new author's affiliation:")
    new_author_country = input("Enter new author's country:")
    new_author_phone = input("Enter new author's phone number:")
    new_author_email_id = input("Enter new author email ID:")
    if new_author_name:
        author.author_name = new_author_name
    if new_author_affiliation:
        author.author_affiliation = new_author_affiliation
    if new_author_country:
        author.author_country = new_author_country
    if new_author_phone:
        author.author_phone = new_author_phone
    if new_author_email_id:
        author.author_email_id = new_author_email_id

def display_all_authors():
    for author in authors.values():
        author.display_author()

while 1:
    print("---Welcome to Library Management System---")
    print("1. Create new user")
    print("2. Create new author")
    print("3. Create new book")
    print("4. Display all users")
    print("5. Display all authors")
    print("6. Display all books")
    print("7. Edit user")
    print("8. Edit author")
    print("9. Edit book")
    print("10. Borrow a book")
    print("11. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        create_new_user()
    if choice == "2":
        create_new_author()
    if choice == "3":
        create_new_book()
    if choice == "4":
        display_all_users()
    if choice == "5":
        display_all_authors()
    if choice == "6":
        display_all_books()
    if choice == "7":
        edit_user()
        display_all_users()
    if choice == "8":
        edit_author()
        display_all_authors()
    if choice == "9":
        edit_book()
        display_all_books()
    if choice == "10":
        user_borrows_books()
    if choice == "11":
        break

print("You have exited the program")