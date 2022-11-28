enunciado = '''Given the dictionary, nested_d, save the medal count for the 
USA from all three Olympics in the dictionary to the list US_count.'''

import json

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

# print(json.dumps(nested_d,indent = 4))
# print(nested_d['Beijing']['Great Britain'])


US_count = []


for lvl1 in nested_d:
    # print(lvl1, '->',nested_d[lvl1])
    for lvl2 in nested_d[lvl1]:
        # print (lvl2, '-->',nested_d[lvl1][lvl2])
        if lvl2 == 'USA':
            US_count.append(nested_d[lvl1][lvl2])
            # print (lvl2, '--->', nested_d[lvl1][lvl2] )
            
print(US_count)

