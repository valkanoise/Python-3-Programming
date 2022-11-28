enunciado = '''The dictionary, medals, shows the medal count for six countries 
during the Rio Olympics. Sort the country names so they appear alphabetically. 
Save this list to the variable alphabetical.'''


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

alphabetical = sorted(medals)

# o también

alphabetical1 = sorted(medals.keys())

print(alphabetical)
print(alphabetical1)


print('alphabetical=alphabetical1', alphabetical==alphabetical1)