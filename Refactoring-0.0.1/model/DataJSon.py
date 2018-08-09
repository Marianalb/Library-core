import json
global f

class JSon():

    def __init__(self,path):
        self.path = path
        #print(self.path)


    def read(self):

        try:
            with open(self.path,'r') as f:

                data = json.load(f)
                return data
        except Exception as e:
                 print("{}").format(str(e))



    def write(self,data):
        try:
            with open(self.path,'w') as f:
                return json.dump(data,f)

        except Exception as e:
            print("{}").format(str(e))




if __name__=="__main__":
 #   books = {"monte dos vendavais": 2, "o nome do vento": 2, "harry potter": 1, "GOT": 2}
  #  clients = {}

    j = JSon()
    jdata = j.read()

    books = jdata
    print books
    #jdata["Peter Pan"]=3

    j.write(jdata)