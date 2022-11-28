enunciado = '''Sort the following list by each element’s second letter a to z. 
Do so by using lambda. Assign the resulting value to the variable lambda_sort'''

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

# def segunda_letra(str1):
#     str1 = str1[1]
#     return str1


lambda_sort = sorted(ex_lst, key = lambda str1 : str1[1])

print(lambda_sort)