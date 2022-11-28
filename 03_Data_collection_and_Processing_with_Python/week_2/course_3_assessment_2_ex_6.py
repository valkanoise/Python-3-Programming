enunciado = '''Write code using zip and filter so that these lists (l1 and l2) 
are combined into one big list and assigned to the variable opposites if they 
are both longer than 3 characters each.'''

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

#versión más corta
opposites5 = filter(lambda tup : len(tup[0]) >= 3 and len(tup[1]) >= 3, list(zip(l1,l2)))
print(list(opposites5))


# lista = list(zip(l1,l2))
# print(lista)

# #usando fiter
# opposites = filter(lambda x : len(x[0]) >= 3 and len(x[1]) >= 3, lista)
# print(list(opposites))


# #usando list comprehension
# # opposites1 = [(x1,x2) for (x1,x2) in lista if len(x1)>=3 and len(x2)>=3]
# # print(opposites1)


#todo junto
# opposites3 = [(x1,x2) for (x1,x2) in list(zip(l1,l2)) if len(x1)>=3 and len(x2)>=3]
# print(opposites3)


