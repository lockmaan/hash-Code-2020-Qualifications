from re import L


class Problem:
    def __init__(self, n, l, D):
        self.n = n
        # number of books
        self.l = l
        # number of libraries
        self.D = D
        # number of days scanning


class Book:
    def __init__(self, n):
        self.score = n
        # the value in scanning that book


class Lib:
    def __init__(self, n, d, c):
        self.n = n
        # the number of books in this library
        self.d = d
        # the duration of the sign up process
        self.c = c
        # the quantity of books that can be shipped per day from this lib
        self.books = []

    def lbooks(self, line):
        self.books = list(map(int, line.split()))
