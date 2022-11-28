enunciado = '''Write a function, sublist, that takes in a list of strings as 
the parameter. In the function, use a while loop to return a sublist of the 
input list. The sublist should contain the same values of the original list 
up until it reaches the string “STOP” (it should not contain the string “STOP”).'''


def sublist(lst_str):
    sublst = []
    idx = 0
    while lst_str[idx] != 'STOP':
        sublst.append(lst_str[idx])
        idx = idx + 1
    return sublst
              
print(sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']))