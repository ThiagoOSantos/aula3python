def votacao():
    Ana = 0
    Bruno = 0
    Carla = 0
    for i in range(5):
        voto= int(input("Em quem você vai votar? Digite 1 para Ana, 2 para Bruno, 3 para Carla"))
        if voto == 1:
            Ana += 1
        elif voto == 2:
            Bruno += 1
        else:
            Carla += 1
        print(f"Ana tirou {Ana} votos, Bruno tirou {Bruno}, e Carla tirou {Carla} votos")
    votacao()