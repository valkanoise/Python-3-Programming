## OJO, esta version no funciona en Python, solo para el examen de coursera
## OJO, esta version no usa API-KEYS para ninguna solicitud!!
## archivo funcional en python se llama 'examen_final_week_3.py'


import requests_with_caching

def get_movies_from_tastedive(string):
    baseurl = 'https://tastedive.com/api/similar'
    params_dict = {}
    params_dict['q'] = string
    params_dict['type'] = 'movies'
    params_dict['limit'] = 5
    response = requests_with_caching.get(baseurl, params = params_dict)
    return response.json()


def extract_movie_titles(data):
    movies = [d['Name'] for d in data['Similar']['Results'] ] #aplico list comprehension
    return movies

    
def get_related_titles(lista_pelis):
    todas_pelis = []
    for peli in lista_pelis:
        titulos = extract_movie_titles(get_movies_from_tastedive(peli))
        for titulo in titulos:
            if titulo not in todas_pelis:
                todas_pelis.append(titulo)
    return todas_pelis

        
def get_movie_data(movie):
    baseurl = 'http://www.omdbapi.com/'
    params_dict = {}
    params_dict['t'] = movie
    params_dict['r'] = 'json'
    response = requests_with_caching.get(baseurl, params = params_dict)
    return response.json()


def get_movie_rating(peli):
    data = peli['Ratings']
    rate = 0
    for dic in data:
        if dic['Source'] == 'Rotten Tomatoes':
            rate = int(dic['Value'].replace('%',''))
        else:
            continue
    return rate
    
def get_sorted_recommendations(list_movies):
    peliculas_relacionadas = get_related_titles(list_movies)
    pelis_y_ratings = {}
    for pelicula in peliculas_relacionadas:
        pelis_y_ratings[pelicula] = get_movie_rating(get_movie_data(pelicula))
    dic_ordenado = sorted(pelis_y_ratings.keys(), key = lambda k : -pelis_y_ratings[k])
    return dic_ordenado
    

