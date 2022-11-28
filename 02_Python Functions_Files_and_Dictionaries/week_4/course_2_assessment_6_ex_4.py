enunciado = '''Write a function called stop_at_z that iterates through a list 
of strings. Using a while loop, append each string to a new list until the 
string that appears is “z”. The function should return the new list.'''

def stop_at_z(lst_str):
    sublst = []
    idx = 0
    while lst_str[idx] != 'z':
        sublst.append(lst_str[idx])
        idx = idx + 1
    return sublst
              
print(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))

