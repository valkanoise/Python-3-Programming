enunciado = '''Create a function called mult that has two parameters, the 
first is required and should be an integer, the second is an optional parameter 
that can either be a number or a string but whose default is 6. The function 
should return the first parameter multiplied by the second.'''

def mult(int, num_str = 6):
    return int * num_str

print(mult(4, 'hello'))
print(mult(3,5))