from model.Param_regex import params_for_regex

global books

def Remover(book_delete):

    book_delete = params_for_regex(book_delete)

    if book_delete not in books:
        print("\nNao foi possivel encontrar o livro\n")
    else:
        del books[book_delete]
