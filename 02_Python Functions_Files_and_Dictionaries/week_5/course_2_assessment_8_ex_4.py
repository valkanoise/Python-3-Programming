enunciado = '''Given the same dictionary, medals, now sort by the medal count.
Save the three countries with the highest medal count to the list, top_three'''


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

countries_sorted = sorted(medals, key = lambda country : medals[country], reverse = True)

top_three = countries_sorted[:3]

for country in medals:
    if country in top_three:
        print (country, medals[country])