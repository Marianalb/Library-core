import DAO
from model.Param_regex import params_for_regex
global clients, books, data_reser

def Requisitar(book,client):

    book = params_for_regex(book)
    client_book =  DAO.Info_DAO.info(book, client)
    client, book = client_book[0],client_book[1]

    if book.name not in books:
        print("\nNao foi possivel encontrar esse livro\n")
    else:

        if books[book.name]["Copys"] > 0:
            if client.name in clients.keys():
                clients[client.name].append({"client id": client.id, "book name": book.name})

            else:
                clients[client.name] = []
                clients[client.name].insert(0, {"client id": client.id, "book name": book.name})




            books[book.name]["Copys"] -= 1
        else:
            print ("\nNao existe livros disponiveis\n")
    if book.name in data_reser.keys():

        data_reser[book.name].append({"client id": client.id, "client name": client.name})

    else:
        data_reser[book.name] = {"client id": client.id, "client name": client.name}






