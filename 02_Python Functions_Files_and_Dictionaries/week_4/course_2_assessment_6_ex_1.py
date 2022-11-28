enunciado = '''Write a function, sublist, that takes in a list of numbers as 
the parameter. In the function, use a while loop to return a sublist of the 
input list. The sublist should contain the same values of the original list 
up until it reaches the number 5 (it should not contain the number 5).'''

def sublist(lista):
    sublista = []
    idx = 0
    while lista[idx] != 5:
        sublista.append(lista[idx])
        idx = idx + 1
    return sublista


