# -*- coding: utf-8 -*-

class Book(object):
    'Book class'

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printMe(self):
        print "Book [id %s | name: %s]" % (self.id, self.name)
