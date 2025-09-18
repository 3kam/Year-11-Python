#This class represent a book in a library.
class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        #Each book contain a unique ID, title, and author.
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

#Class is represented by the borrower who borrow books from the library
class Borrower:
    def __init__(self, borrower_id, name):
        #Each book got its unique ID and name.
        self.borrower_id = borrower_id
        self.name = name

#Class represent a loan, which links to a book to a borrower
class Loan:
    def __init__(self, book, borrower):
        #A loan consisting of the book being borrowed by the borrower.
        self.book = book
        self.borrower = borrower

#Class represents the mangement of the collection of books in the library
class BookManager:
    def __init__(self):
        #Dictionary is stored within the books using their unique book ID as the key
        self.books = {}

#Method to add books to the library
    def add_book(self, book_id, title, author):
        #Ensure book ID is unique before adding and don't have match with other books
        if book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author)

#Method implemented  to remove books from teh system
    def remove_book(self, book_id):
        #Checks if hte borrower ID exist before removing
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

#Method to search books from the borrower by their ID
    def search_book(self, book_id):
        #Return the borrower if found, otherwise return None
        return self.books.get(book_id, None)

#This class manages borrowers book in the library system
class BorrowerManager:
    def __init__(self):
        #Dictionary to store borrowers using their borrower ID as the key
        self.borrowers = {}

#Method to add a new borrower
    def add_borrower(self, borrower_id, name):
        #Ensure that the borrower ID is unique before configuring to the system
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

#Method is to remove the borrower from the system
    def remove_borrower(self, borrower_id):
        #Check if the borrower ID exists before removing
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.")

#Method to search a borrowers by their ID
    def search_borrower(self, borrower_id):
        #Return the borrower if found, otherwise return None
        return self.borrowers.get(borrower_id, None)

#Class mange loans from books to borrowers
class LoanManager:
    def __init__(self):
        #list to store all active loans
        self.loans = []

#Method to create loans on books to be borrowed
#Ensuring that the book is not already loaned beofre creating a new loan
    def create_loan(self, book, borrower):
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        #Creates new loans and store it in the loan list
        loan = Loan(book, borrower)
        self.loans.append(loan)
        #Update book status to indicate it is currently on loan
        book.is_loaned = True

#Method to return a loaned book
    def return_loan(self, book):
        #loop through the active loans to find the matching book
        for loan in self.loans:
            if loan.book.book_id == book.book_id:
                #Remove the loan from the list and update the books status
                self.loans.remove(loan)
                book.is_loaned = False
                break