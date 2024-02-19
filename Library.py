class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        if not book_lines:
            print("No books in the library.")
        else:
            for line in book_lines:
                book_info = line.split(',')
                print(f"Book Name: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' has been added to the library.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        book_list = []
        self.file.seek(0)
        for book in self.file.readlines():
            book_list.append(book.splitlines())
        updated_books = [book for book in book_list if title_to_remove not in book[0].split(',', 1)[0]]
        self.file.seek(0)
        self.file.truncate()

        for updated_book in updated_books:
            self.file.write('\n'.join(updated_book) + '\n')
            print(f"Book '{title_to_remove}' has been removed from the library.")


lib = Library()

# Menu
while True:
    print("\n**** MENU ****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        lib.list_books()
    elif user_choice == "2":
        lib.add_book()
    elif user_choice == "3":
        lib.remove_book()
    elif user_choice == "4":
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")