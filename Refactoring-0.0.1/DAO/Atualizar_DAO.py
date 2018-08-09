import DAO
from model.Param_regex import params_for_regex
global books

def Atualizar(book,new_book_name):

    book = params_for_regex(book)

    if book not in books:
        print("\nNao foi possivel encontrar o nome do livro a atualizar\n")
    else:
        books[new_book_name] = books.pop(book)