enunciado = '''Sort the list ids by the last four digits of each id. Do this 
using lambda and not using a defined function. Save this sorted list in the 
variable sorted_id.'''

# def last_four(idx):
#     idx = str(idx)
#     return idx[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key = lambda idx : str(idx)[-4:])

print(sorted_ids)