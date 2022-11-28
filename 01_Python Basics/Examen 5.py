enunciado = ''' Provided is a list of data about a store's inventory where each 
item in the list represents the name of an item, how much is in stock, and how 
much it costs. Print out each item in the list with the same formatting, using 
the .format method (not string concatenation). For example, the first print 
statment should read The store has 12 shoes, each for 29.99 USD.'''

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for i in inventory:
    list = i.split(', ') # separo por ,_ y espacio. Los saca en la lista tupl
    item = list[0]
    quantity = list[1]
    price = list[2]
    print('The store has {} {}, each for {} USD.'.format(quantity,item,price))
    

print('--------otra opcion--------')
#solución 'pythonica'
for i in inventory:
        print('The store has {} {}, each for {} USD.'.format(i.split(", ")[1],i.split(", ")[0],i.split(", ")[2]))
        

print('--------otra opcion--------')
#otra opción sin format y concatenando strings
for i in inventory:
    print('The store has ' + i.split(", ")[1] + ' ' + i.split(", ")[0] + ', each for ' + i.split(", ")[2] + ' USD')