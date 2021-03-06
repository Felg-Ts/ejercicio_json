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

def searhinfo(chfile):

    print('''
    1-mage
    2-support
    3-ranged
    4-recomended
    5-carry
    6-melle
    ''')

    ctags = input("Introduce el nombre de una tag: ")

    if ctags == '1':
        print('Los champions que contienen la tag mage son:' ,chfile['Champion'][0]['name'])
    elif ctags == '2':
        print('Los champions que contienen la tag support son:' ,chfile['Champion'][0]['name'] ,chfile['Champion'][1]['name'])
    elif ctags == '3':
        print('Los champions que contienen la tag ranged son:' ,chfile['Champion'][0]['name'] ,chfile['Champion'][1]['name'] )
    elif ctags == '4':
        print('Los champions que contienen la tag recomended son:' ,chfile['Champion'][1]['name'] ,chfile['Champion'][2]['name'])
    elif ctags == '5':
        print('Los champions que contienen la tag carry son:' ,chfile['Champion'][2]['name'])
    elif ctags == '6':
        print('Los champions que contienen la tag melee son:' ,chfile['Champion'][2]['name'])
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('cls')