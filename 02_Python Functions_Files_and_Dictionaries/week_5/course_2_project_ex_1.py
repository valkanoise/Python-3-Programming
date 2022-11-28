punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#funcion que saca todos los caracteres de puntuacion de un string
def strip_punctuation (str1):
    for punct in punctuation_chars:
        if punct in str1:
            str1 = str1.replace(punct, '')
    return str1

#funcion que calcular cuantas palabras del string son positivas, y previamente le saco los puntos de puntuacion
def get_pos(string):
    count = 0
    string = strip_punctuation(string)
    for word in string.split():
        if word.lower() in positive_words:
            count = count + 1
    return count

#funcion que calcular cuantas palabras del string son negativas, y previamente le saco los puntos de puntuacion
def get_neg(string):
    count = 0
    string = strip_punctuation(string)
    for word in string.split():
        if word.lower() in negative_words:
            count = count + 1
    return count

# # list of positive words to use
# positive_words = []
# with open("positive_words.txt") as pos_f:
#     for lin in pos_f:
#         if lin[0] != ';' and lin[0] != '\n':
#             positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
file = open('project_twitter_data.csv', 'r')
print(file.read())