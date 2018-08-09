from model.DataJSon import JSon
from model.Client import Client

class Reservas_DAO(object):

    def __init__(self):

        file = JSon("/media/sf_VMshared/Refactoring1/Resources/Reservas.json")
        self.reserv = file.read()

    def get_reserv(self):
        return self.reserv

    def get_clients_from_book(self,book):
        names=[]
        i =len(self.reserv[book])

        if i >= 2:
            for index in range(i):
                aux = self.reserv[book][index]
                names.append(aux["client name"])
            return names
        else:
            return self.reserv[book][i-1]["client name"]

    def get_id_from_book(self,book):
        id = []
        i = len(self.reserv[book])

        if i >= 2:
            for index in range(i):
                aux = self.reserv[book][index]
                id.append(aux["client id"])
            return id
        else:
            return self.reserv[book][i - 1]["client id"]

    def get_book_from_id(self,id):
        for key in self.reserv.keys():
            arr= self.get_id_from_book(key)
            if(type(arr)!=list):
                if(id == arr):
                    return key
            else:
                for index in range(len(arr)):
                    if (id == arr[index]):
                        return key
        print ("Nao foi possivel encontrar um livro com esse id")

    def get_book_from_client(self,client):
        for key in self.reserv.keys():
            if(client in self.get_clients_from_book(key)):
                return key
        print ("Nao foi possivel encontrar um livro com esse cliente")

    def append_clients(self,book_name,client):
        self.reserv[book_name] += [{"client id": client.id, "client name": client.name}]

    def set_clients(self,client):
        if client.book in self.reserv:
            self.reserv[client.book] += [{"client id": client.id, "client name": client.name}]
        else:
            self.reserv[client.book] = [{"client id": client.id, "client name": client.name}]


if __name__ == '__main__':
     f = Reservas_DAO()
     cl = Client(10, "euzinha", "Harry Potter")
     f.set_clients(cl)
     f
     f = f.get_reserv()
     print(f)

