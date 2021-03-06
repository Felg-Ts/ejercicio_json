import json
import funciones
opción = "11"

chfile = json.loads(open('champions.json').read())

while opción >= "1" and opción <= "5":

    print('''
    1-Lista los nombres de los champions con sus correspondientes habilidades.
    2-Cuantos champions hay en el fichero.
    3-Pide por teclado una tags y muestra a los champions que la tienen.
    4-Pide por teclado la habilidad de cualquier champion y muestra a quien pertenece.
    5-Pide por teclado el nombre de un champion, muestra por pantalla sus habilidades, 
    selecciona una de las habilidades y muestra su descripción.
    ''')

    opción = input("Introduce un número del 1 al 5 para ejecutar una de las 5 funciones: ")

    if opción == '1':
        funciones.listinfo(chfile)
    elif opción == '2':
        funciones.countinfo(chfile)
    elif opción == '3':
        funciones.searhinfo(chfile)
    elif opción == '4':
        funciones.searhinfore(chfile)
    elif opción == '5':
        funciones.searhichamabil(chfile)
