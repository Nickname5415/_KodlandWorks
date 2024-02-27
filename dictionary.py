print("Hola estimado usuari@, este  es un diccionario de palabras actuales como LOL")
for i in range(5):
    
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "GG": "Significa Good Game, es decir Buen Juego y sirve como reaccion positiva despues de una partida, usualmente para videojuegos",
                "BFF": "Significa Best Friends Forever, en español Mejores Amigos Por Siempre, usualmente es usada para mostrar una buena amistad",
                "CREEPY": "aterrador, siniestro",
                "AGGRO": "Ponerse agresivo/enojado"
                }
            
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")            

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Esta palabra no se ha encontrado, intente con otra")
