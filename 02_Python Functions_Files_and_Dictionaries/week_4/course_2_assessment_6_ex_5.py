enunciado = '''Below is a for loop that works. Underneath the for loop, rewrite 
the problem so that it does the same thing, but using a while loop instead of 
a for loop. Assign the accumulated total in the while loop code to the variable 
sum2. Once complete, sum2 should equal sum1.'''

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
    
print(sum1)

sum2 = 0
idx = 0

while idx < len(lst):
    sum2 = sum2 + lst[idx]
    idx = idx + 1

print(sum2)

print('Son sum1 y sum2 iguales?', sum1 == sum2)

