"""Konverter Basis Bilangan.ipynb

# Muhammad Rafly Ash Shiddiqi
## 235150207111062
## Teknik Informatika E
"""

def binerKeDesimal(biner):
    desimal = int(biner)
    return desimal

def desimalKeBiner(desimal):
    biner = bin(desimal)
    return biner

def binerKeHexa(biner):
    hexa = hex(biner)
    return hexa

def hexaKeBiner(hexa):
    biner = bin(hexa)
    return biner

def desimalKeHexa(desimal):
    hexa = hex(desimal)
    return hexa

def hexaKeDesimal(hexa):
    desimal = int(hexa)
    return desimal

menu = [
    'Keluar',
    'Biner ke Desimal',
    'Desimal ke Biner',
    'Biner ke Hexa',
    'Hexa ke Biner',
    'Desimal ke Hexa',
    'Hexa ke Desimal',
]

while True:
    print('KONVERTER BASIS BILANGAN')
    for i in range(len(menu)):
        print(f'{i}. {menu[i]}')

    pilihan = input('Masukkan pilihan anda: ')
    if pilihan == '0':
        break
    elif pilihan == '1':
        biner = int(input('Masukkan bilangan biner: '), 2)
        print(binerKeDesimal(biner))
    elif pilihan == '2':
        desimal = int(input('Masukkan bilangan desimal: '))
        print(desimalKeBiner(desimal))
    elif pilihan == '3':
        biner = int(input('Masukkan bilangan biner: '), 2)
        print(binerKeHexa(biner))
    elif pilihan == '4':
        hexa = int(input('Masukkan bilangan hexa: '), 16)
        print(hexaKeBiner(hexa))
    elif pilihan == '5':
        desimal = int(input('Masukkan bilangan desimal: '))
        print(desimalKeHexa(desimal))
    elif pilihan == '6':
        hexa = int(input('Masukkan bilangan hexa: '), 16)
        print(hexaKeDesimal(hexa))
    else:
        print('Input tidak valid!')
