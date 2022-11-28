enunciado = '''Write a function called check_nums that takes a list as its 
parameter, and contains a while loop that only stops once the element of the 
list is the number 7. What is returned is a list of all of the numbers up until 
it reaches 7.'''

def check_nums(lst):
    lista = []
    idx = 0
    while lst[idx] != 7:
        lista.append(lst[idx])
        idx = idx + 1
    return lista


print(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]))