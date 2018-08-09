from model.Client import Client
from model.DataJSon import JSon



class Client_DAO(object):


    def __init__(self):
        file = JSon("/media/sf_VMshared/Refactoring1/Resources/Clients.json")
        self.dic_client = file.read()

    def get_clients(self):
        return self.dic_client


    def get_clientID_from_name(self,name):
        return self.dic_client[name]["id"]

    def get_clientBooks_from_name(self,name):
        return self.dic_client[name]["book name"]

    def get_clientName_from_id(self,id):
        for key in (self.dic_client):
            if (self.dic_client[key]["client id"] == id):
                return key

    def get_clientName_from_bookName(self,book):
        names=[]
        for key in (self.dic_client.keys()):
            if(book in self.dic_client[key]["book name"]):
                names.append(key)


        if names:
            return names
        else:
            print "Nao existe clientes com esse livro"

    def set_id_client(self,key,id):
         self.dic_client[key]["client id"] = id
         return self.dic_client

    def set_book_name(self, key, bookname):
        self.dic_client[key]["book name"] = bookname
        return self.dic_client
#if __name__=="__main__":
 #   f = Client_DAO()
  #  print f.get_clients()

   # print f.get_clientName_from_bookName("Harry Potter")