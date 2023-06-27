opc = 0
asientos = [
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.'],
        [ '.','.','.','.','.','.','.','.','.','.']
]
def mostrar_menu():
    print('0.agregar pelicula')
    print('1.peliculas')
    print('2.comprar entrada')
    print('3.salir')


def agregar_pelicula():
    nombre = input('ingrese el nombre de la pelicula')
    pelicula = (nombre)
    pelicula.append(pelicula )
       
def peliculas():
    print('unica pelicula en cartelera')
    nombre = ('spiderman-lejos de casa') 
       


def comprar_entrada():
    entrada = 0
    num_asiento = 0
    seleccion = int(input('que pelicula desea ver:'))
    num_entradas = int(input('solamente se pueden comprar una entrada por persona'))
    peliculas = peliculas[seleccion - 1]
    precio = 2500
    print ('escoja su asuento')
    while num_asiento > 0 :
        print(num_asiento)
        for fila in range(15):
            for columna in range(10): 
                print(f'[{asientos[fila][columna]}] ', end='')
        print('')    
    fila = int(input('ingrese la fila'))
    columna = int(input('ingrese la columna'))
   


     


while True: 
    mostrar_menu()
    if opc == '0':
        agregar_pelicula()
    elif opc == '1':
        peliculas()  
    elif opc == '2':
        comprar_entrada()
    else :
        print('opccion no valida')
        break          


    
   