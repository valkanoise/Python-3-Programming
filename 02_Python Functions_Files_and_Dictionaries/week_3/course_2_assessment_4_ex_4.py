enunciado = '''Write a function, accum, that takes a list of integers as 
input and returns the sum of those integers.'''

def accum(lst_int):
    suma = 0
    for int in lst_int:
        suma = suma + int
    return suma