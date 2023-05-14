"""
Menu 1:
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
6. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
7. Calcular e informar cual es el superhéroe más y menos pesado.

"""
import os

def menu():
    print(" ------------------------------------------------------")
    print("|               *** STARK INDUSTRIES ***               |")
    print("|------------------------------------------------------|")
    print("|1- listar heroes                                      |")
    print("|2- Lista de heroes con su altura                      |")
    print("|3- determinar heroe mas alto                          |")
    print("|4- determinar heroe mas bajo                          |")
    print("|5- Promedio de altura                                 |")
    print("|6- Informar asociados al maximo y minimo de altura    |")
    print("|7- Calcular e informar heroe mas y menos pesado       |")
    print("|8- Mas opciones                                       |")
    print("|9- Salir                                              |")
    print(" ------------------------------------------------------")
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            break
        except ValueError:
            input("Error. Ingrese una opcion valida")
    return opcion


def cargarLista(list_destino, list_origen):

    for item in list_origen:
        list_destino.append(item)


def mostrarPersonas(lista):
    print(" ________________________________________________________________________________________________________________________________________________________________")
    print("|                                                                  *** lista de personas ***                                                                     |")
    print("|________________________________________________________________________________________________________________________________________________________________|")
    print("|   NOMBRE                 |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    for personas in lista:
        print(f'|{personas["nombre"]:25s} | {personas["identidad"]:30s} | {personas["empresa"]:12s} | {personas["altura"]:.5} | {personas["peso"]:.5} | {personas["genero"]:2s}   | {personas["color_ojos"]:23s} | {personas["color_pelo"]:13s} | {personas["fuerza"]:3s}  | {personas["inteligencia"]:10s} |')
    print("|________________________________________________________________________________________________________________________________________________________________|")


def mostrarPersonasAlturas(lista):
    print(' ---------------------------------------------------')
    print('|         Nombre             |          Altura      |')
    print('|---------------------------------------------------|')
    for personas in lista:
        print(
            f'| Nombre: {personas["nombre"]:18s} |      Altura: {personas["altura"]:.5}   |')
    print(' ---------------------------------------------------')


def personajeAlto(lista):

    personaje_alto = lista[0]

    for persona in lista:
        if (float(persona["altura"]) > float(personaje_alto["altura"])):
            personaje_alto = persona

    if (personaje_alto != lista[0]):

        print(' ___________________________________________________')
        print('|                 Altura mas alta                   |')
        print('|---------------------------------------------------|')
        print(f'|Altura: {personaje_alto["altura"]:.5}                                      |')
        print('|___________________________________________________|')
        return personaje_alto
    else:
        print("No se pudo determinar el personaje mas alto!")
        return 0


def personajeBajo(lista):

    personaBajo = lista[0]

    for persona in lista:
        if (float(persona["altura"]) < float(personaBajo["altura"])):
            personaBajo = persona

    if (personaBajo != 100):

        print(' ___________________________________________________')
        print('|                 Altura mas baja                   |')
        print('|---------------------------------------------------|')
        print(f'|Altura: {personaBajo["altura"]:.5}                                         |')
        print('|___________________________________________________|')
        return personaBajo
    else:
        print("No se pudo determinar el personaje mas bajo!")
        return 0
    


def calcularPromedio(lista):

    suma = 0

    for personas in lista:
        suma += float(personas["altura"])

    promedio = suma / len(lista)

    print(' ___________________________________________________')
    print('|               El promedio de altura es            |')
    print('|---------------------------------------------------|')
    print(f'|  El promedio de altura es: {promedio:.2f}                 |')
    print('|___________________________________________________|')

def filtrar_pesos(lista):

    personajeP = lista[0]
    personajeL = lista[0]

    for persona in lista:
        if (float(persona["peso"]) > float(personajeP["peso"])):
            personajeP = persona

    print(" _________________________________________________________________________")
    print("|                                                                         |")
    print(f'|El superheroe mas pesado es: {personajeP["nombre"]} con {personajeP["peso"]:.5} de peso                      |')
    print("|_________________________________________________________________________|")

    for persona in lista:
        if (float(persona["peso"]) < float(personajeL["peso"])):
            menos_pesado = persona

    print(" _________________________________________________________________________")
    print("|                                                                         |")
    print(f'|El superheroe menos pesado es: {menos_pesado["nombre"]} con {menos_pesado["peso"]:.5} de peso                   |')
    print("|_________________________________________________________________________|")


def mostrarNombres(texto1, texto2, alto, bajo, dato, key2):

    print(' ___________________________________________________')
    print(f"                  Heroe mas {texto1}                ")
    print('|---------------------------------------------------|')
    print(
        f'| Nombre: {alto["nombre"]:18s} |      {dato}: {alto[key2]:.5}   |')
    print('|___________________________________________________|')    

    print(' ___________________________________________________')
    print(f"                  Heroe mas {texto2}                ")
    print('|---------------------------------------------------|')
    print(
        f'| Nombre: {bajo["nombre"]:18s} |      {dato}: {bajo[key2]:.5}   |')
    print('|___________________________________________________|')





"""
Menu 2:
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
5. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
6. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
7. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
8. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
9. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
12. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
13. Listar todos los superhéroes agrupados por color de ojos.
14. Listar todos los superhéroes agrupados por color de pelo.
15. Listar todos los superhéroes agrupados por tipo de inteligencia

"""


def submenu2(lista):

    
    while True:
        os.system("cls")
        print(" _____________________________________________")
        print("|         *** STARK INDUSTRIES ***            |")
        print("|            -----Sub Menu-----               |")
        print("|---------------------------------------------|")
        print("|1- Listar genero masculino                   |")
        print("|2- Listar genero femenino                    |")
        print("|3- Determinar masculino mas alto             |")
        print("|4- Determinar femenina mas alta              |")
        print("|5- Determinar masculino mas bajo             |")
        print("|6- Determinar femenina mas baja              |")
        print("|7- Calcular promedio de altura masculino     |")
        print("|8- Calcular promedio de altura femenino      |")
        print("|9- Informar nombres de los puntos 3 a 6      |")
        print("|10- Determinar color de ojos                 |")
        print("|11- Determinar color de pelo                 |")
        print("|12- Determinar tipo de inteligencia          |")
        print("|13- Listar por color de ojos                 |")
        print("|14- Listar por color de pelo                 |")
        print("|15- Listar por tipo de inteligencia          |")
        print("|20- Volver al menu principal                 |")
        print("|_____________________________________________|")
    
    
        try:
            opcion = int(input("Ingrese opcion: "))
        except ValueError:
            input("Error. Ingrese una opcion valida")
        
        
        match(opcion):

            case 1:
                mostrarPersonasFyM(lista, 'M', "masculino")

            case 2:
                mostrarPersonasFyM(lista, 'F', "femenino")

            case 3:
                AlturasGenero(lista, "m", "alto")

            case 4:
                AlturasGenero(lista, "f", "alto")

            case 5:
                AlturasGenero(lista, "m", "bajo")

            case 6:
                AlturasGenero(lista, "f", "bajo")

            case 7:
                PromedioAlturaGenero(lista, "m", "masculino")

            case 8:
                PromedioAlturaGenero(lista, "f", "femenino")

            case 9:
                mostrarAlturas(AlturasGenero(lista, "m", "alto"), AlturasGenero(lista, "f", "alto"), AlturasGenero(lista, "m", "bajo"), AlturasGenero(lista, "f", "bajo"))

            case 10:
                determinarColorOjos(lista)

            case 11:
                determinarColorPelo(lista)

            case 12:
                determinarInteligencia(lista)

            case 13:
                informarPorColorOjos(lista)

            case 14:
                informarPorColorPelo(lista)

            case 15:
                informarPorInteligencia(lista)

            case 20:
                break
        os.system("pause")




def mostrarPersonasFyM(lista, genero, titulo):
    print(" ________________________________________________________________________________________________________________________________________________________________")
    print(f"                                                                  *** Listado de genero {titulo} ***                                                             ")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|    NOMBRE                |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|________________________________________________________________________________________________________________________________________________________________|")

    for personas in lista:
        if (personas["genero"] == genero):
            print(f'|{personas["nombre"]:25s} | {personas["identidad"]:30s} | {personas["empresa"]:12s} | {personas["altura"]:.5} | {personas["peso"]:.5} | {personas["genero"]:2s}   | {personas["color_ojos"]:23s} | {personas["color_pelo"]:13s} | {personas["fuerza"]:3s}  | {personas["inteligencia"]:10s} |')
    print("|________________________________________________________________________________________________________________________________________________________________|")




def AlturasGenero(lista, genero, orden: str):

    
    altura_x = None
    
    for persona in lista:
        if persona["genero"] == genero.upper():
            altura_x = persona
            break
    
    if altura_x is None:
        print(f"No se encontró ninguna persona del género {genero} en la lista.")
        return -1

    if(orden.lower() == "alto"):
        for persona in lista:
            if (persona["genero"] == genero.upper() and float(persona["altura"]) > float(altura_x["altura"])):
                altura_x = persona
    elif(orden.lower() == "bajo"):
        for persona in lista:
            if (persona["genero"] == genero.upper() and float(persona["altura"]) < float(altura_x["altura"])):
                altura_x = persona
    else:
        print("Ingreso una altura invalida!")
        return -1

    print(' ___________________________________________________')
    print('|         Nombre             |          Altura      |')
    print('|---------------------------------------------------|')
    print(
        f'| Nombre: {altura_x["nombre"]:18s} |      Altura: {altura_x["altura"]:.5}   |')
    print('|___________________________________________________|')
    
    return altura_x


def PromedioAlturaGenero(lista, genero, titulo: str):

    suma = 0
    contador = 0

    for persona in lista:
        if (persona["genero"] == genero.upper()):
            suma += float(persona["altura"])
            contador += 1

    promedio = suma / contador

    if (suma != 0):
        print(' ___________________________________________________________________')
        print(f'|                         promedio {titulo}                        |')
        print('|-------------------------------------------------------------------|')
        print(
            f'| Promedio: {promedio:.2f}                                                    |')
        print('|___________________________________________________________________|')
    else:
        print("No se pudo calcular el promedio!")


def mostrarAlturas(masculinoAlto, femeninaAlta, masculinoBajo, femeninaBaja):

    if (masculinoAlto != None and femeninaAlta != None and masculinoBajo != None and femeninaBaja != None):
        print(' ___________________________________________________________________')
        print('|                         Masculino mas alto                        |')
        print('|-------------------------------------------------------------------|')
        print(
            f'|   Nombre: {masculinoAlto["nombre"]:.18s} | Altura: {masculinoAlto["altura"]:5.5}                                   |')
        print('|___________________________________________________________________|')

        print(' ___________________________________________________________________')
        print('|                         Femenina mas Alta                         |')
        print('|-------------------------------------------------------------------|')
        print(
            f'|   Nombre: {femeninaAlta["nombre"]:.18s} | Altura: {femeninaAlta["altura"]:5.5}                                  |')
        print('|___________________________________________________________________|')

        print(' ___________________________________________________________________')
        print('|                         Masculino mas bajo                        |')
        print('|-------------------------------------------------------------------|')
        print(
            f'|   Nombre: {masculinoBajo["nombre"]:.18s} | Altura: {masculinoBajo["altura"]:5.5}                         |')
        print('|___________________________________________________________________|')

        print(' ___________________________________________________________________')
        print('|                         Femenina mas baja                         |')
        print('|-------------------------------------------------------------------|')
        print(
            f'|   Nombre: {femeninaBaja["nombre"]:.18s} | Altura: {femeninaBaja["altura"]:5.5}                             |')
        print('|___________________________________________________________________|')
    else:
        print("No se pudieron mostrar los datos!")


def determinarColorOjos(lista):
    
    colores_ojos = {
        "Brown": 0,
        "Blue": 0,
        "Green": 0,
        "Hazel": 0,
        "Yellow": 0,
        "Silver": 0,
        "Red": 0,
        "Yellow (without irises)": 0
    }

    for persona in lista:
        color_ojos = persona["color_ojos"]
        if color_ojos in colores_ojos:
            colores_ojos[color_ojos] += 1

    print(' ____________________________________________________')
    print('| Brown | Blue | Green |Hazel |Yellow | Silver | Red |')
    print('|----------------------------------------------------|')
    print(
        f'| {colores_ojos["Brown"]}     |{colores_ojos["Blue"]}     |{colores_ojos["Green"]}      |{colores_ojos["Hazel"]}     |{colores_ojos["Yellow"]}      |{colores_ojos["Silver"]}       |{colores_ojos["Red"]}    |')
    print('|____________________________________________________|')



def determinarColorPelo(lista):
    
    contador_colores = {
        "Green": 0,
        "Brown": 0,
        "Auburn": 0,
        "Black": 0,
        "Yellow": 0,
        "Red / Orange": 0,
        "Red": 0,
        "Brown / White": 0,
        "White": 0,
        "Blond": 0,
        "No Hair": 0
    }

    for persona in lista:
        color_pelo = persona["color_pelo"]
        if color_pelo in contador_colores:
            contador_colores[color_pelo] += 1
        else:
            contador_colores[color_pelo] = 1

    contador_colores

    print(' __________________________________________________________________________________________________')
    print('| Brown | Black | Green |Auburn |Yellow | Red/Orange | Red | white | No hair | Blond | Brown/White |')
    print('|--------------------------------------------------------------------------------------------------|')
    print(f'| {contador_colores["Brown"]}     |{contador_colores["Black"]}      |{contador_colores["Green"]}      |{contador_colores["Auburn"]}      |{contador_colores["Yellow"]}      |{contador_colores["Red / Orange"]}           |{contador_colores["Red"]}    |{contador_colores["White"]}      |{contador_colores["No Hair"]}        |{contador_colores["Blond"]}      |{contador_colores["Brown / White"]}            |')
    print('|__________________________________________________________________________________________________|')




def determinarInteligencia(lista):
    
    contador = {"good": 0, "average": 0, "high": 0, "": 0}
    
    for persona in lista:
        inteligencia = persona.get("inteligencia", "").lower()
        if inteligencia == "good":
            contador["good"] += 1
        elif inteligencia == "average":
            contador["average"] += 1
        elif inteligencia == "high":
            contador["high"] += 1
        else:
            contador[""] += 1
            persona["inteligencia"] = "No Tiene"
    print(' __________________________________________________')
    print('|   Good   |   Average   |   High   |   No tiene   |')
    print('|--------------------------------------------------|')
    print(f'| {contador["good"]:>5}    |{contador["average"]:>5}        |{contador["high"]:>5}     |{contador[""]:>5}         |')
    print('|__________________________________________________|')


def informarPorColorOjos(lista):

    print(' ________________________________________________________________________________________________________________________________________________________________')
    print('|                                                                   Listado por color de ojos                                                                    |')
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print("|    NOMBRE                |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    personas_por_color = []
    color_ojos = []
    
    for persona in lista:
        personas_por_color.append(persona.copy())

    for heroe in personas_por_color:
        if not esta_en_lista(color_ojos, heroe["color_ojos"]):
            color_ojos.append(heroe["color_ojos"])
    
    for color in color_ojos:
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f'|                                                                {color:10.10}                                                                                  |')
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for persona in personas_por_color:
            if(persona["color_ojos"] == color):
                print(f'|{persona["nombre"]:25s} | {persona["identidad"]:30s} | {persona["empresa"]:12s} | {persona["altura"]:.5} | {persona["peso"]:.5} | {persona["genero"]:2s}   | {persona["color_ojos"]:23s} | {persona["color_pelo"]:13s} | {persona["fuerza"]:3s}  | {persona["inteligencia"]:10s} |')
    print('|________________________________________________________________________________________________________________________________________________________________|')


def informarPorColorPelo(lista):

    print(' ________________________________________________________________________________________________________________________________________________________________')
    print('|                                                                   Listado por color de pelo                                                                    |')
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print("|    NOMBRE                |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    
    personas_por_pelo = []
    color_pelo = []

    for persona in lista:
        personas_por_pelo.append(persona.copy())

    for heroe in personas_por_pelo:
        if not esta_en_lista(color_pelo, heroe["color_pelo"]):
            color_pelo.append(heroe["color_pelo"])

    for color in color_pelo:
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f'|                                                                {color:10.10}                                                                                  |')
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for persona in personas_por_pelo:
            if(persona["color_pelo"] == color):
                print(f'|{persona["nombre"]:25s} | {persona["identidad"]:30s} | {persona["empresa"]:12s} | {persona["altura"]:.5} | {persona["peso"]:.5} | {persona["genero"]:2s}   | {persona["color_ojos"]:23s} | {persona["color_pelo"]:13s} | {persona["fuerza"]:3s}  | {persona["inteligencia"]:10s} |')
    print('|________________________________________________________________________________________________________________________________________________________________|')


def informarPorInteligencia(lista):

    print(' ________________________________________________________________________________________________________________________________________________________________')
    print('|                                                                   Listado por inteligencia                                                                     |')
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print("|    NOMBRE                |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    
    
    personas_por_inteligencia = []
    inteligencias = []

    for persona in lista:
        if(persona["inteligencia"] == ""):
            persona["inteligencia"] = "No tiene"
        
    for persona in lista:
            personas_por_inteligencia.append(persona.copy())

    for heroe in personas_por_inteligencia:
        if not esta_en_lista(inteligencias, heroe["inteligencia"]):
            inteligencias.append(heroe["inteligencia"])

    for inteligencia in inteligencias:
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f'|                                                                {inteligencia:10.10}                                                                                      |')
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for persona in personas_por_inteligencia:
            if(persona["inteligencia"] == inteligencia):
                print(f'|{persona["nombre"]:25s} | {persona["identidad"]:30s} | {persona["empresa"]:12s} | {persona["altura"]:.5} | {persona["peso"]:.5} | {persona["genero"]:2s}   | {persona["color_ojos"]:23s} | {persona["color_pelo"]:13s} | {persona["fuerza"]:3s}  | {persona["inteligencia"]:10s} |')
    print('|________________________________________________________________________________________________________________________________________________________________|')


def esta_en_lista(lista: list, item: str)->bool:
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta



