#funciones
#def name_function
# code

#funcion sin parametros
#funcion sin retorno
def saluda():
    print("Hola Developers!")

saluda()

#parametros, sin retorno
def duplica(number):
    print(number*2)

duplica(23)

def suma(num1, num2):
    print(num1 + num2)

suma (12+34)

# parametros opcionales 
def lista_drinks(d1="beer", d2 ="water"):
    print(d1)
    print(d2)

lista_drinks("tequila","juice")
lista_drinks("tequila")
lista_drinks()
lista_drinks(d2='soda',d1="vodka")
