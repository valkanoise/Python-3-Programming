enunciado = '''Provided is a buggy for loop that tries to accumulate some 
values out of some dictionaries. Insert a try/except so that the code 
passes.'''


di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    #es una lista de diccionarios y un diccionario no tiene el key 'Puppies'
    try:
        total = total + diction['Puppies']
    except KeyError:
        pass
print("Total number of puppies:", total)