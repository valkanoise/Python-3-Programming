funcion = ''' SCRIPT PARA INGRESAR UNA LISTA DE PELIS, Y DEVUELVE LISTA DE 
5 PELIS RELACIONADAS Y LAS ORDENA SEGUN LA CALIFICACION DE ROTTEN TOMATOES
Y SI HAY EMPATE POR ORDEN ALFABETICO'''
## OJO, esta versión usa API-KEYS para tastedive y OMDb.
## OTO, esta versión no usa requests_with_caching.
## OJO, esta versión funciona haciendo requests verdaderos

import requests

## primera parte ##
def get_movies_from_tastedive(string):
    baseurl = 'https://tastedive.com/api/similar'
    params_dict = {}
    params_dict['k'] = '378289-Valkanoi-B9FLKFKJ'
    params_dict['q'] = string
    params_dict['type'] = 'movies'
    params_dict['limit'] = 10
    response = requests.get(baseurl, params = params_dict)
    return response.json()


##segunda parte ##
def extract_movie_titles(data):
    movies = [d['Name'] for d in data['Similar']['Results'] ] #aplico list comprehension
    return movies


## tercera parte ##
    
def get_related_titles(lista_pelis):
    todas_pelis = []
    for peli in lista_pelis:
        titulos = extract_movie_titles(get_movies_from_tastedive(peli))
        for titulo in titulos:
            if titulo not in todas_pelis:
                todas_pelis.append(titulo)
    return todas_pelis

        
## cuarta parte ##
    
def get_movie_data(movie):
    baseurl = 'http://www.omdbapi.com/'
    params_dict = {}
    params_dict['apikey'] = 'a3a69b87'
    params_dict['t'] = movie
    params_dict['r'] = 'json'
    response = requests.get(baseurl, params = params_dict)
    return response.json()


## quinta parte ##
def get_movie_rating(peli):
    data = peli['Ratings']
    rate = 0
    for dic in data:
        if dic['Source'] == 'Rotten Tomatoes':
            rate = int(dic['Value'].replace('%',''))
        else:
            continue
    return rate

## sexta parte ##
def get_sorted_recommendations(list_movies):
    peliculas_relacionadas = get_related_titles(list_movies)
   
# # Si quiero hacer un diccionario de {'Pelicula': 'rating'}    
#     pelis_y_ratings = {}
#     for pelicula in peliculas_relacionadas:
#         pelis_y_ratings[pelicula] = get_movie_rating(get_movie_data(pelicula))
#     dic_ordenado = sorted(pelis_y_ratings.keys(), key = lambda k : -pelis_y_ratings[k])
#     return dic_ordenado

#Si quiero hacer una lista de tuples [(Pelicula, rating)]      
    pelis_y_ratings = []
    for pelicula in peliculas_relacionadas:
        pelis_y_ratings.append((pelicula, get_movie_rating(get_movie_data(pelicula))))
    lista_ordenada = sorted(pelis_y_ratings, key = lambda x : (-x[1],x[0]))
    return lista_ordenada


##ACÁ SE PONEN LAS PELICULAS QUE SE QUIEREN BUSCAR
x = get_sorted_recommendations(["The Adventures of Buckaroo Banzai Across the 8th Dimension"])

for tup in x:
    print('Peli:', tup[0], 'Rating:', tup[1])

