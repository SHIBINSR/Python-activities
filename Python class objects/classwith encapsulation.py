class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.cart = {}  # Dictionary to store product objects

    def add_product(self, product):
        if product.name in self.cart:
            # If the product already exists, increase its quantity
            self.cart[product.name].quantity += product.quantity
        else:
            # Otherwise, add it to the dictionary
            self.cart[product.name] = product

    def show_cart(self):
        print("\nShopping Cart:")
        for product in self.cart.values():  # Get product objects from dictionary
            print(f"{product.name} - {product.quantity} x {product.price} = {product.total_price()}")

# Creating products
b = Product("Laptop", 50000, 1)
m = Product("Mouse", 1500, 2)
k = Product("Keyboard", 2500, 1)

# Using OOP
cart = ShoppingCart()
cart.add_product(b)
cart.add_product(m)
cart.add_product(k)

# Adding another mouse (to test quantity update)
cart.add_product(Product("Mouse", 1500, 3))

# Display the cart
cart.show_cart()

print(library)
 
library.remove_book("Python Programming")
print(library)
 
print("Books by John Smith:")
john_books = library.find_books_by_author("John Smith")
for book in john_books:
    print(book)
    
    class Library:
    def __init__(self, name):
        self.name = name
        print(self.name)
        self.books = {}
        
    def add_book(self, book):
        self.books[book.title] = book
        
    def get_books(self):
        return list(self.books)
      
    def remove_book(self, book_title):
        if book_title in self.books:
            del self.books[book_title]
            print(f"Book '{book_title}'' was deleted from the library")
        else:
            print(f"Book '{book_title}' not found in the library.")
 
    def find_books_by_author(self, author):
        for book in self.books.values():
            if book.author==author:
                print(book.author,"-",book.title)
             
        
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
library = Library("oxford")

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science Handbook", "Jane Doe")
book3 = Book("Algorithms and Data Structures", "John Smith")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
 
print(library.get_books())

library.remove_book("fdsf")
library.remove_book("Python Programming")
library.remove_book("Python Programming")

print(library.get_books())

library.add_book(Book("Cristiano Ronaldo","Shibin R Silva"))
library.add_book(Book("Cristiano Ronaldo biography","John Smith"))

print(library.get_books())

library.find_books_by_author("John Smith")

