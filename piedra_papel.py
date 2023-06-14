#eleccion de Maquina
import random

num_rand=random.randint(1,3)
if num_rand ==1:
    choice_maq='piedra'
elif num_rand == 2:
    choice_maq='Papel'
else :
    choice_maq ='Tijeras'


# Eleccion de Usuario
choice_text = '''
Escribe una Opcion
    Piedra
    Papel
    Tijeras
'''
choice_user = input (choice_text)

# Imprime Seleccion

print("Usuario Elije: ", choice_user)
print("Maquina Elije: ", choice_maq)

#Define ganador
if choice_user == choice_maq:
    print("Es un empate")
else:
    if choice_user == 'Piedra' and choice_maq == 'papel':
        print("Gana maquina")
    elif choice_user == 'Piedra' and choice_maq == 'Tijeras':
        print("Gana usuario")
    elif choice_user == 'Papel' and choice_maq == 'Piedra':
        print("Gana Maquina")
    elif choice_user == 'Papel' and choice_maq == 'Tijeras':
        print("Gana Maquna")
    elif choice_user == 'Tijeras' and choice_maq == 'Piedra':
        print("Gana Usuario")
    else:
        print("Escribe bien Usuario") 