#crear repo git y clonar
#subir repo el siguiente ejercicio:
#programa python que solicita 5 notas
#guarda las notas en una lista 
#muestra el promedio(debe ser función)


#funcion leer nota
def funcion_leer_nota(dato):
    while True:
        try:
            nota = float(input(dato))
            if 1 <= nota <= 7:
                return nota
            else:
                print("La nota debe estar entre 1 y 7.")
        except:
            print("Debe ingresar un número válido.")

#Función para calcular promedio
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / cantidad       

# --- PROGRAMA PRINCIPAL ---

notas = []

try:
    cantidad = int(input("¿Cuántos notas desea registrar?: "))
except:
    print("Debe ingresar un número válido.")
    cantidad = 0

