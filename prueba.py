from pathlib import Path
import json
import csv
import os
from modules.constru import construir_menu, sol_ans
from modules.elimi import soli_codi, eliminar
from modules.agregando import agregar
home=Path(__file__).parent.parent
jsonf=Path(home/'base.json')
rutac=Path(home/'mandarina.csv')


while True:
    construir_menu(menup='')
    ans=sol_ans()
    if ans =='1':
        with open (jsonf, mode='r') as stream:
            json_file= json.dump(stream)
        codigo=input("ingrese el codigo o  para buscar la pintura")
        nom=input("ingrese el nombre o  para buscar la pintura")
        ans=input(f'Esta seguro?, es{codigo}?\nsi.1:\nno.2:')
        for codigo in jsonf or nom in jsonf:
            print(codigo)
            print(nom)
    elif ans=='2':
         pass
    elif ans =='3':
        agregar
    elif ans =='4':
        soli_codi(eliminar) 
    elif ans=='5':
        if not jsonf.exists() or jsonf.stat().st_size == 0:
            print('Esta vacio el json')
        else:
            rutac.unlink()
            rutac.touch()
        with open(jsonf, mode='r')as stream:
            json_file= json.load(stream)
            for pintura in json_file:
                datto={codigo["codigo"],
                       pintura["nombre"]}
    else:
        os.system('cls')
        exit('Error elige opcion valida')
        