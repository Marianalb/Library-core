from model.RegularExpression import RegularExpression
global books

def params_for_regex(book_name):
    arr_book = []
    for book_aux in books.keys():
        arr_book.append(book_aux)
    #print(arr_book)
    for index in range(len(arr_book)):
        arr_book[index] = arr_book[index].replace('', '*')
        aux = arr_book[index].replace(' *', ' ')
        arr_book[index] = aux[1:]

    word = RegularExpression(arr_book, book_name[0:]).apply()
    word = word.replace('*', '')
    return word
