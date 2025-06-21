

def solicitar_nota():
    while True:
        try:
            numero = float(input('Ingresar nota: '))
            if numero >= 1 and numero <= 7:
                return numero
        except:
            print('nota debe ser numero')

def calcular_promedio(lista):
    sumatoria = 0
    for i in lista:
        sumatoria+=i
    return sumatoria/len(lista)

#programa principal
notas = []
for i in range(5):
    nota = solicitar_nota ()
    notas.append(nota)
    promedio = calcular_promedio(nota)
    print(f'promedio: {promedio}')


