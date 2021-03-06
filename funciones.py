import msvcrt
import os

def listinfo(chfile):
    for i in chfile['Champion']:
        print('Champion-name:' ,i['name'])
        print('Habilidad-pasiva:' ,i['abilities']['Ability'][0]['name'])
        print('Habilidad-1:' ,i['abilities']['Ability'][1]['name'])
        print('Habilidad-2:' ,i['abilities']['Ability'][2]['name'])
        print('Habilidad-3:' ,i['abilities']['Ability'][3]['name'])
        print('Habilidad-4:' ,i['abilities']['Ability'][4]['name'])
        print('')
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('cls')

def countinfo(chfile):

    contch = len(chfile['Champion'])

    print(f'En el fichero se encuentran un total de: {contch} champions')

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('cls')
