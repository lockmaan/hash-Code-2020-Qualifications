from matplotlib.style import library
from Classes import *


def Readata(file_path):

    lines = open(file_path).readlines()
    problem = Problem(*list(map(int, lines[0].split())))
    books = Book(*list(map(int, lines[1].split())))
    libraries = []

    for i in range(2, problem.l+2, 2):
        lib = Lib(int(lines[1].split()))
        lib.lbooks(lines[i+1])
        libraries.append(lib)

    return problem, books, libraries
