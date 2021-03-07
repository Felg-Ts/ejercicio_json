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
    os.system('clear')

def countinfo(chfile):

    contch = len(chfile['Champion'])

    print(f'En el fichero se encuentran un total de: {contch} champions')

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

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
    os.system('clear')

def searhinfore(chfile):

    print('''
    1-Illumination
    2-Light Binding
    3-Prismatic Barrier
    4-Lucent Singularity
    5-Final Spark
    6-Consecration
    7-Starcall
    8-Astral Blessing
    9-Infuse
    10-Wish
    11-Double Strike
    12-Alpha Strike
    13-Meditate
    14-Wuju Style
    15-Highlander
    ''')

    ctags = input("Introduce el nombre de una habilidad: ")

    #habilidades Lux
    if ctags == 'Illumination' or ctags == 'Light Binding':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][0]['name'])
    elif ctags == 'Prismatic Barrier' or ctags == 'Lucent Singularity':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][0]['name'])
    elif ctags == 'Final Spark':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][0]['name'])

    #habilidades Soraka
    elif ctags == 'Consecration' or ctags == 'Starcall':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][1]['name'])
    elif ctags == 'Astral Blessing' or ctags == 'Infuse':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][1]['name'])
    elif ctags == 'Wish':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][1]['name'])

    #habilidades Master yi
    elif ctags == 'Double Strike' or ctags == 'Alpha Strike':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][2]['name'])
    elif ctags == 'Meditate' or ctags == 'Wuju Style':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][2]['name'])
    elif ctags == 'Highlander':
        print(f'La habilidad {ctags} pertenece a:' ,chfile['Champion'][2]['name'])

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

def searhichamabil(chfile):

    print('''
    1-Lux
    2-Soraka
    3-MasterYi
    ''')

    nchamp = input("Introduce el nombre de un champion: ")


    #habilidades Lux

    if nchamp == (chfile['Champion'][0]['name']):

        print('''
        1-Illumination
        2-Light Binding
        3-Prismatic Barrier
        4-Lucent Singularity
        5-Final Spark
        ''')

        abiln = input("Introduce el nombre de una habilidad de Lux para ver su descripción: ")

        if abiln == (chfile['Champion'][0]['abilities']['Ability'][0]['name']):
            print(chfile['Champion'][0]['abilities']['Ability'][0]['description'])
        elif abiln == (chfile['Champion'][0]['abilities']['Ability'][1]['name']):
            print(chfile['Champion'][0]['abilities']['Ability'][1]['description'])
        elif abiln == (chfile['Champion'][0]['abilities']['Ability'][2]['name']):
            print(chfile['Champion'][0]['abilities']['Ability'][2]['description'])
        elif abiln == (chfile['Champion'][0]['abilities']['Ability'][3]['name']):
            print(chfile['Champion'][0]['abilities']['Ability'][3]['description'])
        elif abiln == (chfile['Champion'][0]['abilities']['Ability'][4]['name']):
            print(chfile['Champion'][0]['abilities']['Ability'][4]['description'])

    #habilidades Soraka

    elif nchamp == (chfile['Champion'][1]['name']):

        print('''
        1-Consecration
        2-Starcall
        3-Astral Blessing
        4-Infuse
        5-Wish
        ''')

        abiln = input("Introduce el nombre de una habilidad de Soraka para ver su descripción: ")

        if abiln == (chfile['Champion'][1]['abilities']['Ability'][0]['name']):
            print(chfile['Champion'][1]['abilities']['Ability'][0]['description'])
        elif abiln == (chfile['Champion'][1]['abilities']['Ability'][1]['name']):
            print(chfile['Champion'][1]['abilities']['Ability'][1]['description'])
        elif abiln == (chfile['Champion'][1]['abilities']['Ability'][2]['name']):
            print(chfile['Champion'][1]['abilities']['Ability'][2]['description'])
        elif abiln == (chfile['Champion'][1]['abilities']['Ability'][3]['name']):
            print(chfile['Champion'][1]['abilities']['Ability'][3]['description'])
        elif abiln == (chfile['Champion'][1]['abilities']['Ability'][4]['name']):
            print(chfile['Champion'][1]['abilities']['Ability'][4]['description'])


    #habilidades MasterYi

    elif nchamp == (chfile['Champion'][2]['name']):

        print('''
        1-Double Strike
        2-Alpha Strike
        3-Meditate
        4-Wuju Style
        5-Highlander
        ''')

        abiln = input("Introduce el nombre de una habilidad de Soraka para ver su descripción: ")

        if abiln == (chfile['Champion'][2]['abilities']['Ability'][0]['name']):
            print(chfile['Champion'][2]['abilities']['Ability'][0]['description'])
        elif abiln == (chfile['Champion'][2]['abilities']['Ability'][1]['name']):
            print(chfile['Champion'][2]['abilities']['Ability'][1]['description'])
        elif abiln == (chfile['Champion'][2]['abilities']['Ability'][2]['name']):
            print(chfile['Champion'][2]['abilities']['Ability'][2]['description'])
        elif abiln == (chfile['Champion'][2]['abilities']['Ability'][3]['name']):
            print(chfile['Champion'][2]['abilities']['Ability'][3]['description'])
        elif abiln == (chfile['Champion'][2]['abilities']['Ability'][4]['name']):
            print(chfile['Champion'][2]['abilities']['Ability'][4]['description'])

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')
