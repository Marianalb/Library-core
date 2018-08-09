# -*- coding: utf-8 -*-

class Client(object):
    'Client class'

    def __init__(self, id, name, book):
        self.id = id
        self.name = name
        self.book = book

    def printMe(self):
        print "Client [id %s | name: %s | Book name: %s]" % (self.id, self.name, self.book.name)