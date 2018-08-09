import DAO
from model.Param_regex import params_for_regex

global clients, books, data_reser



def Adicionar(book):

  #  book = params_for_regex(book)
    print book
    client_book =  DAO.Info_DAO.info(book, "Administrador")
    book = client_book[1]

    if book.name in books:
        books[book.name]["Copys"] += 1
    else:
        books[book.name] = {"id": book.id, "Copys": 1}
