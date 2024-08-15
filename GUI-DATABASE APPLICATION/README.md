Bookstore Management System
Overview
This project is a simple graphical user interface (GUI) application for managing a bookstore's database. Built using Python's Tkinter for the GUI and SQLite for database management, this application allows users to view, search, add, update, and delete book records. The GUI provides an intuitive way to interact with the database and manage book entries efficiently.

Features
View All Books: Displays a list of all books in the database.
Search for Books: Allows users to search for books based on title, author, year, or ISBN.
Add New Books: Enables users to add new book entries to the database.
Update Existing Books: Allows users to update details of existing book records.
Delete Books: Provides functionality to remove books from the database.
GUI Interface: Built with Tkinter, offering a user-friendly interface for interacting with the database.
Installation
Requirements
Python 3.x
Tkinter (comes with Python standard library)
SQLite (comes with Python standard library)
Setup
Clone the Repository:

git clone https://github.com/yourusername/bookstore-management.git
cd bookstore-management

Install Dependencies:

There are no additional Python packages required as the project uses built-in libraries.

Run the Application:

Navigate to the project directory and run the interface.py file:

python interface.py

Usage
GUI Components
Labels and Entry Fields: For entering book details (Title, Author, Year, ISBN).
Listbox: Displays the list of books from the database.
Buttons:
View All: Displays all books in the Listbox.
Search Entry: Searches for books based on the input fields.
Add Entry: Adds a new book to the database.
Update: Updates the selected book's details.
Delete: Deletes the selected book from the database.
Close: Closes the application.
Example
Viewing All Books:
Click the "View all" button to display all books in the Listbox.

Adding a New Book:
Enter the book details into the entry fields and click "Add entry" to insert the new book into the database.

Searching for a Book:
Enter search criteria into the fields and click "Search entry" to find matching books.

Updating a Book:
Select a book from the Listbox, modify the details in the entry fields, and click "Update" to apply the changes.

Deleting a Book:
Select a book from the Listbox and click "Delete" to remove it from the database.

Code Description
main.py
Purpose: Contains the Tkinter-based GUI application to interact with the SQLite database.
Functions:
select_row(event): Handles row selection in the Listbox and updates entry fields.
view_data(): Fetches and displays all book records from the database.
search_data(): Searches the database based on user input and updates the Listbox.
add_data(): Inserts a new book record into the database and updates the Listbox.
delete_data(): Deletes the selected book from the database.
update_data(): Updates the details of the selected book in the database.
data.py
Purpose: Manages SQLite database operations for the bookstore.
Functions:
connect(): Establishes a connection to the SQLite database and creates the book table if it doesn't exist.
insert(title, author, year, isbn): Inserts a new book record into the database.
view(): Retrieves all book records from the database.
search(title, author, year, isbn): Searches for books based on the provided criteria.
delete(id): Deletes a book record based on the provided ID.
update(id, title, author, year, isbn): Updates a book record with new details based on the provided ID.

Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request or open an issue.

Contact
For any questions or feedback, please contact [pramodkumar23la@gmail.com].
