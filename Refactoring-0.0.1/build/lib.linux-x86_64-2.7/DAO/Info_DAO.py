from model.Book import Book
from model.Client import Client

global books,clients

def info(book_name,client_name):



    book_id = len(books)
    book = Book(book_id, book_name)
    book.printMe()

    client_id = len(clients)
    client = Client(client_id, client_name, book)
    client.printMe()
    return [client,book]