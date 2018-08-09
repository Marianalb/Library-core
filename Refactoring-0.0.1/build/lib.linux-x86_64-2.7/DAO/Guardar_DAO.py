global clients, books, data_reser


def Guardar(clients_file,book_file,f):

    clients_file.write(clients)
    book_file.write(books)
    f.write(data_reser)