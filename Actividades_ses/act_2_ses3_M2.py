nombreynota = input("Introduce tu nombre y nota (separados por un espacio): ")
nombre, nota = nombreynota.split()
nota = float(nota)

if nota>=60:
     print(f'{nombre} ha aprobado con: {calificación}')
else:
     print(f'{nombre} no ha aprobado, su calificación es: {calificación}')

##################
while nombreynota != "fin":
    nombreynota = input("Introduce tu nombre y nota (separados por un espacio): ")
    if nombreynota == "fin":
        break
    nombre, nota = nombreynota.split()
    nota = float(nota)

    if nota >= 60:
        print(f'{nombre} ha aprobado con: {nota}')
    else:
        print(f'{nombre} no ha aprobado, su calificación es: {nota}')

#####################
nombreynota =()
while nombreynota != "fin":
    nombreynota = input("Introduce nombre y nota matematicas, ciencias e inglés (separados por un espacio): ")
    if nombreynota == "fin":
        break
    nombre, matematica, ciencias, ingles = nombreynota.split()
    matematica = float(matematica)
    ciencias = float(ciencias)
    ingles = float(ingles)
    nota = (matematica + ciencias + ingles) / 3
    if nota >= 60:
        print(f'{nombre} ha aprobado con: {nota}')
    else:
        print(f'{nombre} no ha aprobado, su calificación es: {nota}')
    
##################
nombreynota =()
nota = 0
while nombreynota != "fin":
    nombreynota = input("Introduce nombre y nota matematicas, ciencias e inglés (separados por un espacio): ")
    if nombreynota == "fin":
        break
    nombre, matematica, ciencias, ingles = nombreynota.split()
    nombre= str(nombre)
    matematica = float(matematica)
    ciencias = float(ciencias)
    ingles = float(ingles)

    nota = (matematica + ciencias + ingles) / 3

    #Evaluar aprobación
    if nota >= 60:
        print(f'{nombre} ha aprobado con promedio: {nota}')
    else:
        print(f'{nombre} no ha aprobado, su promedio es: {nota}')

    #Asignar calificación cualitativa
    if nota>= 90:
        calificación = "Excelente"
    elif nota >=75 and nota <=89:
         calificación = "Bueno"
    else:
        calificación = "Necesita mejorar"
    print(f'{nombre} ha obtenido una calificación de: {calificación}\n')

###################

nombreynota = ()
alumnos=[]
while nombreynota != "fin":
    nombreynota = input("Introduce nombre y nota Mat., Cs e ing. (separados por un espacio): ")
    if nombreynota == "fin":
        break

    nombre, matematica, ciencias, ingles = nombreynota.split()
    matematica = float(matematica)
    ciencias = float(ciencias)
    ingles = float(ingles)
    alumnos.append({"nombre": nombre,
                    "matematica": matematica,
                    "ciencias": ciencias, 
                    "ingles": ingles})

for alumno in alumnos:
    nombre = alumno["nombre"]
    nota = (alumno["matematica"] + alumno["ciencias"] + alumno["ingles"]) / 3

    #Evaluar aprobación
    if nota >= 60:
     print(f'{nombre} ha aprobado con promedio: {nota}')
    else:
      print(f'{nombre} no ha aprobado, su promedio es: {nota}')

    #Asignar calificación cualitativa
    if nota>= 90:
        calificación = "Excelente"
    elif nota >=75 and nota <=89:
         calificación = "Bueno"
    else:
        calificación = "Necesita mejorar"
    print(f'{nombre} obtuvo un promedio de:{nota} | Comentarios: {calificación}\n')
 #Expresión ternaria
    Mensaje = "¡Puntuación perfecta!" if nota == 100 else "¡Sigue practicando!"
    print(Mensaje)
######
##6. Expresión ternaria
