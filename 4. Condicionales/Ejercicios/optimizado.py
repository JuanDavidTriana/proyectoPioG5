dia = 1
mes = 12

if not(1 <= mes <= 12 and 1 <= dia <= 31):
    print("Fecha no válida")
else:
    signos = [
        ("Capricornio", (12, 22), (1, 19)),
        ("Acuario", (1, 20), (2, 18)),
        ("Piscis", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Tauro", (4, 20), (5, 20)),
        ("Géminis", (5, 21), (6, 20)),
        ("Cáncer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Escorpio", (10, 23), (11, 21)),
        ("Sagitario", (11, 22), (12, 21))
    ]

    for signo, (mes_inicio, dia_inicio), (mes_fin, dia_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            print(signo)
            break
