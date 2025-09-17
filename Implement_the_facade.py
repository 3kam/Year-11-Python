if __name__ == "__main__":
    library = LibraryFacade()

    # Adding books
    library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(2, "1984", "George Orwell")

    # Adding borrowers
    library.add_borrower(1, "Alice")
    library.add_borrower(2, "Bob")

    # Creating a loan
    library.create_loan(1, 1)  # Alice borrows "The Great Gatsby"

    # Searching for a book
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")

    # Returning a loan
    library.return_loan(1)

    # Checking the book status again
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")