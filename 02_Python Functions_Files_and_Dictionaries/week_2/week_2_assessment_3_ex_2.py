enunciado = '''Create a dictionary, freq, that displays each character in 
string str1 as the key and its frequency as the value.'''

str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] = freq[char] + 1

print(freq)