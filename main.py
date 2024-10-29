while True:
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "ROFL": "Una respuesta a una broma",
                "SHEESH": "Ligera desapobración",
                "CREPPY": "Alternado, siniestro",
                "AGGRO": "Ponerse agresivo/enojado"
            }
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No existe en el momento")
