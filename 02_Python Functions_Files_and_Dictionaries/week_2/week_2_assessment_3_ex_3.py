enunciado = '''Provided is a string saved to the variable name s1. Create a 
dictionary named counts that contains each letter in s1 and the number of 
times it occurs.'''

s1 = "hello"
counts = {}

for char in s1:
    if char not in counts:
        counts[char] = 0
    counts[char] = counts[char] + 1
    
 
print(counts)