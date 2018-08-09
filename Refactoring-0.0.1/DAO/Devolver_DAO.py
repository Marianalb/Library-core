import DAO
from model.Param_regex import params_for_regex

global clients, books, data_reser

def Devolver(book,client):

    book = params_for_regex(book)
    client_book =  DAO.Info_DAO.info(book, client)
    client, book = client_book[0],client_book[1]

    if (book.name not in books and client.name not in clients):
        print("\nNao e possivel devolver o livro\n")

    else:
        books[book.name]["Copys"] +=1

