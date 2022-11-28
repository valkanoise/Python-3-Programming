enunciado = '''The list, numb, contains integers. Write code that populates 
the list remainder with the remainder of 36 divided by each number in numb. 
For example, the first element should be 0, because 36/6 has no remainder. 
If there is an error, have the string “Error” appear in the remainder.'''


numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []

for num in numb:
    try:
        remainder.append(36 % num)
    except ZeroDivisionError:
        remainder.append('Error')
        
print(remainder)