import math
from datetime import datetime, timedelta
class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.inventory:
            self.inventory[book_id] = {
                'title': title,
                'author': author,
                'borrowed': False,
                'borrow_date': None,
                'due_date': None
            }
            print(f"Book '{title}' added to inventory.")
        else:
            print("Book ID already exists.")

    def remove_book(self, book_id):
        if book_id in self.inventory:
            removed_book = self.inventory.pop(book_id)
            print(f"Book '{removed_book['title']}' removed from inventory.")
        else:
            print("Book not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for book_id, details in self.inventory.items():
            status = "Borrowed" if details['borrowed'] else "Available"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")


class BorrowReturnManager:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager
        self.borrow_duration_days = 14  

    def borrow_book(self, book_id):
        book = self.inventory_manager.inventory.get(book_id)
        if book and not book['borrowed']:
            book['borrowed'] = True
            book['borrow_date'] = datetime.now()
            book['due_date'] = datetime.now() + timedelta(days=self.borrow_duration_days)
            print(f"Book '{book['title']}' borrowed successfully. Due date is {book['due_date'].date()}.")
        else:
            print("Book is either not available or already borrowed.")

    def return_book(self, book_id):
        book = self.inventory_manager.inventory.get(book_id)
        if book and book['borrowed']:
            book['borrowed'] = False
            book['borrow_date'] = None
            book['due_date'] = None
            print(f"Book '{book['title']}' returned successfully.")
        else:
            print("Book is not currently borrowed or not found.")

    def check_availability(self, book_id):
        book = self.inventory_manager.inventory.get(book_id)
        if book:
            return not book['borrowed']
        else:
            print("Book not found.")
            return False

def calculate_fine(days_late, fine_per_day=1.5):
    return math.ceil(days_late) * fine_per_day if days_late > 0 else 0

def get_overdue_books(inventory):
    now = datetime.now()
    overdue_books = list(filter(lambda b: b['borrowed'] and b['due_date'] < now, inventory.values()))
    return overdue_books

def borrowed_books_report(inventory):
    return [book for book in inventory.values() if book['borrowed']]

if __name__ == "__main__":
    inventory_manager = InventoryManager()
    borrow_return_manager = BorrowReturnManager(inventory_manager)

    inventory_manager.add_book(1, "1984", "George Orwell")
    inventory_manager.add_book(2, "To Kill a Mockingbird", "Harper Lee")
    inventory_manager.add_book(3, "The Great Gatsby", "F. Scott Fitzgerald")

    inventory_manager.display_inventory()

    borrow_return_manager.borrow_book(1)

    print(f"Is book 1 available? {borrow_return_manager.check_availability(1)}")

    borrow_return_manager.return_book(1)

    fine = calculate_fine(5)
    print(f"Fine for 5 days late return: ${fine}")


    borrow_return_manager.borrow_book(2)

    inventory_manager.inventory[2]['due_date'] = datetime.now() - timedelta(days=1)

    overdue_books = get_overdue_books(inventory_manager.inventory)
    print("Overdue books:")
    for book in overdue_books:
        print(f"- {book['title']}")

    report = borrowed_books_report(inventory_manager.inventory)
    print("Borrowed Books Report:")
    for book in report:
        print(f"- {book['title']} by {book['author']}")
