enunciado = '''Find the least frequent letter. Create the dictionary characters 
that shows each character from string sally and its frequency. Then, find the 
least frequent letter in the string and assign the letter to the variable 
worst_char.'''

sally = "sally sells sea shells by the sea shore and by the road"


characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] = characters[char] + 1
    
keys = list(characters.keys())
#print(keys)
worst_char = keys[0]

for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key

print(characters)        
print(worst_char)


