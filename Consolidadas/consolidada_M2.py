#Definición de variables y tipos de datos.
libreria = [{'título':'Robinson Crusoe','autor':'Daniel Defoe', 'precio':5000, 'stock':10},  ##Para esto se deben usar corchetes porque es una cadena de diccionarios.
            {'título':'Ante la bandera','autor':'Julio Verne', 'precio':7000, 'stock':5},
            {'título':'El principito','autor':'Antoine de Saint-Exupéry', 'precio':6000, 'stock':8},
            {'título':'1984','autor':'George Orwell', 'precio':8000, 'stock':2},
            {'título':'Papelucho','autor':'Marcela Paz', 'precio':4000, 'stock':15}]


#Definición de función mostrar_libros_disponibles()
def mostrar_libros_disponibles():
    for libro in libreria:
        if libro.get("stock")>1:  #con .get se accede al valor
            print(libro)

mostrar_libros_disponibles()

#Solicitar al usuario ingresar un rango de precio y mostrar en pantalla
minimo = float(input("Ingrese un precio mínimo:"))  ##debe ingresarse un float porque los precios son decimales.
maximo = float(input("Ingrese un precio máximo:"))

for libro in libreria:
    if libro.get('precio')>=minimo and libro.get('precio')<=maximo:
        print(libro)
    elif libro.get('precio')<=minimo and libro.get('precio')>=maximo:
        print('No disponible')