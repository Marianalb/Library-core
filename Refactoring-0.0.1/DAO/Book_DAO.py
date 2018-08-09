from model.Book import Book
from model.DataJSon import JSon


class Book_DAO(Book):

    def __init__(self):
        global file
        file = JSon("/media/sf_VMshared/Refactoring1/Resources/Book")
        self.dic_book = file.read()


    def get_dic_book(self):
        return self.dic_book

    def get_book_name_from_id(self, id):

           for key in (self.dic_book):
               if(self.dic_book[key]["id"] == id):
                   return key

           print "Nao existe um livro com esse id"


    def get_book_id_from_name(self,name):
        for i in range(len(self.dic_book)):
            if name == self.get_book_name_from_id(i):
                return i

        print("Nao existe um livro com esse nome")

    def get_book_name_from_numberOfCopys(self,number_copy):

        book_names=[]
        for key in (self.dic_book):
            if (self.dic_book[key]["Copys"] == number_copy):
                book_names.append( key)

        if book_names:
            return book_names
        else:
            print "Nao existe um livro com esse id"

    def get_numberOfCopys_from_name(self,name):
        return self.dic_book[name]["Copys"]

    def set_id(self,key,id):
        if key in self.dic_book:
            self.dic_book[key][0]["id"] = id
        else:
            self.dic_book[key] = [{"Copys":1,"id":id}]

    def set_copy(self,key,copy):
        if key in self.dic_book:
            self.dic_book[key]["Copys"] = copy
        else:
            self.dic_book[key] = [{"Copys":1,"id":len(self.dic_book)}]

