enunciado = '''A palindrome is a phrase that, if reversed, would read the exact 
same. Write code that checks if p_phrase is a palindrome by reversing it and 
then checking if the reversed version is equal to the original. Assign the 
reversed version of p_phrase to the variable r_phrase so that we can check 
your work.''' 

p_phrase = "was it a car or a cat I saw"

r_phrase = ''

for letter in p_phrase:
    r_phrase = letter + r_phrase
    
print(r_phrase)
print('Is p_phrase a palindrome?', p_phrase == r_phrase)