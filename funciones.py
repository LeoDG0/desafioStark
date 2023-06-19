from data_stark import lista_personajes
import os


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


def cargarLista(list_destino: list, list_origen: list):

    for item in list_origen:
        list_destino.append(item)


def mostrarPersonas(lista: list):
    print(" ________________________________________________________________________________________________________________________________________________________________")
    print("|                                                                  *** lista de personas ***                                                                     |")
    print("|________________________________________________________________________________________________________________________________________________________________|")
    print("|   NOMBRE                 |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    for personas in lista:
        print(f'|{personas["nombre"]:25s} | {personas["identidad"]:30s} | {personas["empresa"]:12s} | {personas["altura"]:.5} | {personas["peso"]:.5} | {personas["genero"]:2s}   | {personas["color_ojos"]:23s} | {personas["color_pelo"]:13s} | {personas["fuerza"]:3s}  | {personas["inteligencia"]:10s} |')
    print("|________________________________________________________________________________________________________________________________________________________________|")


def mostrarPersonasAlturas(lista: list):
    print(' ---------------------------------------------------')
    print('|         Nombre             |          Altura      |')
    print('|---------------------------------------------------|')
    for personas in lista:
        print(
            f'| Nombre: {personas["nombre"]:18s} |      Altura: {personas["altura"]:.5}   |')
    print(' ---------------------------------------------------')


def personajeAlto(lista: list):

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


def personajeBajo(lista: list):

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
    


def calcularPromedio(lista: list):

    suma = 0

    for personas in lista:
        suma += float(personas["altura"])

    promedio = suma / len(lista)

    print(' ___________________________________________________')
    print('|               El promedio de altura es            |')
    print('|---------------------------------------------------|')
    print(f'|  El promedio de altura es: {promedio:.2f}                 |')
    print('|___________________________________________________|')

def filtrar_pesos(lista: list):

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


def submenu2(lista: list):

    
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
                informarPorClave(lista, "color_ojos")

            case 14:
                informarPorClave(lista, "color_pelo")

            case 15:
                informarPorClave(lista, "inteligencia")

            case 20:
                break
        os.system("pause")





def mostrarPersonasFyM(lista: list, genero, titulo):
    print(" ________________________________________________________________________________________________________________________________________________________________________")
    print(f"|                                                                      *** Listado de genero {titulo} ***                                                               |")
    print("|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|    NOMBRE                |     identidad                  |  empresa      |altura  | peso   |genero|      color de ojos        |  color de pelo  |fuerza  |inteligencia|")
    print("|________________________________________________________________________________________________________________________________________________________________________|")

    for personas in lista:
        if (personas["genero"] == genero):
            print(f'|{personas["nombre"]:25} | {personas["identidad"]:30} | {personas["empresa"]:12} | {personas["altura"]:6} | {personas["peso"]:6} | {personas["genero"]:2}   | {personas["color_ojos"]:25} | {personas["color_pelo"]:15} | {personas["fuerza"]:5}  | {personas["inteligencia"]:10} |')
    print("|________________________________________________________________________________________________________________________________________________________________________|")




def AlturasGenero(lista: list, genero, orden: str):

    
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


def PromedioAlturaGenero(lista: list, genero, titulo: str):

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


def determinarColorOjos(lista: list):
    
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



def determinarColorPelo(lista: list):
    
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




def determinarInteligencia(lista: list):
    
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


def informarPorClave(lista: list, key:str):
    print(' ________________________________________________________________________________________________________________________________________________________________')
    print(f'|                                                                   Listado por {key}                                                                   |')
    print('|----------------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print("|    NOMBRE                |     identidad                  |  empresa      |altura | peso  |genero|      color de ojos      |color de pelo  |fuerza|inteligencia|")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    personas_por_clave = []
    valores_clave = []

    for persona in lista:
        personas_por_clave.append(persona.copy())

    for persona in personas_por_clave:
        if persona[key] not in valores_clave:
            valores_clave.append(persona[key])

    for valor in valores_clave:
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f'|                                                                {valor:10.10}                                                                                  |')
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for persona in personas_por_clave:
            if persona[key] == valor:
                print(f'|{persona["nombre"]:25} | {persona["identidad"]:30} | {persona["empresa"]:12} | {persona["altura"]:6} | {persona["peso"]:6} | {persona["genero"]:2}   | {persona["color_ojos"]:25} | {persona["color_pelo"]:15} | {persona["fuerza"]:5}  | {persona["inteligencia"]:10} |')
    print('|________________________________________________________________________________________________________________________________________________________________|')



def esta_en_lista(lista: list, item: str)->bool:
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta


#03

#1

def obtener_nombre(lista: list):
        
    nombre = lista.get("nombre", "")
    nombre_formateado = f"Nombre: {nombre}"
    
    return nombre_formateado


def imprimir_dato(nombre: str):
    print(nombre)







#2

def obtener_nombre_y_dato(lista: list, key: str):
    
    nombre = lista.get("nombre", "")

    for clave, valor in lista.items():
        if clave == key:
            heroe = f"Nombre: {nombre:18} |{clave}: {valor}"
            return heroe #devuelve el heroe
    
    return None #si no encuentra nada devuelve none







#4

def calcular_max(lista: list, key: str):

    if not lista:
        return None
    
    max_valor = None
    heroe_max = None

    for heroe in lista:
        valor = heroe.get(key)

        if valor is None:
            return 0
        else:
            if max_valor is None or valor > max_valor:
                max_valor = valor
                heroe_max = heroe
    
    return heroe_max

def calcular_min(lista: list, key: str):

    if not lista:
        return None
    
    min_valor = None
    heroe_min = None

    for heroe in lista:
        valor = heroe.get(key)

        if valor is None:
            return 0
        else:
            if min_valor is None or valor < min_valor:
                min_valor = valor
                heroe_min = heroe
                

    return heroe_min


def calcular_max_min_dato(lista: list, dato_a_calcular: str, key: str):

    if(dato_a_calcular == "maximo"):
        heroe_max = calcular_max(lista, key)
        return heroe_max
    elif(dato_a_calcular == "minimo"):
        heroe_min = calcular_min(lista, key)
        return heroe_min
    else:
        return None





#5.1

def sumar_dato_heroe(lista: list, key: str):
    
    suma = 0

    for heroe in lista:
        if(type(heroe) == dict and key in heroe):
            if(heroe[key] is not None):
                suma += heroe[key]
    
    return suma



#5.2

def dividir(dividendo: int, divisor: int):
    
    try:
        int(dividendo)
        int(divisor)
    except ValueError:
        print("Los parametros deben ser numeros enteros!")
        
    if(divisor == 0):
        return 0
    else:
        division = dividendo / divisor
        return division


#5.3

def calcular_promedio(lista: list, key:str):

    promedio = 0
    cantidad = 0

    suma = sumar_dato_heroe(lista, key)

    for heroe in lista:
        cantidad += 1
    
    if(cantidad > 0):
        promedio = dividir(suma, cantidad)
        return promedio
    else:
        return 0
    








#6.1


def imprimir_menu_002():
    
    imprimir_dato("""  ------------------------------------------------------
 |               *** STARK INDUSTRIES ***               |
 |------------------------------------------------------|
 |1- listar heroes                                      |
 |2- Lista de heroes con su altura                      |
 |3- determinar heroe mas alto                          |
 |4- determinar heroe mas bajo                          |
 |5- Promedio de altura                                 |
 |6- Informar asociados al maximo y minimo de altura    |
 |7- Calcular e informar heroe mas y menos pesado       |
 |8- Mas opciones                                       |
 |9- Salir                                              |
  ------------------------------------------------------""")
    


#6.2

def validar_entero(numero:str):
    
    try:
        int(numero)
        return True
    except ValueError:
        return False


#04

#1.1

def extraer_iniciales(nombre_heroe: str):
    if nombre_heroe == "":
        return "N/A"

    nombre_heroe = nombre_heroe.replace("-", " ")
    palabras = nombre_heroe.split()

    iniciales = ""
    for palabra in palabras:
        if palabra.lower() != "the":
            iniciales += palabra[0].upper() + "."
    
    return iniciales


#1.2

def definir_iniciales_nombre(heroe:dict):
    if type(heroe) != dict:
        return False
    
    if 'nombre' not in heroe:
        return False
    
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    return True


#1.3

def agregar_iniciales_nombre(lista: list):
    if type(lista) != list:
        return False
    
    if len(lista) == 0:
        return False
    
    for heroe in lista:
        if not definir_iniciales_nombre(heroe):
            print("El origen de datos no contiene el formato correcto")
            return False
    
    return True




#2.1

def generar_codigo_heroe(id_heroe, genero_heroe: str):
    if not isinstance(id_heroe, int) or genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    
    codigo_genero = genero_heroe + "-"
    codigo_id = str(id_heroe).zfill(8)
    codigo_final = codigo_genero + codigo_id

    if(len(codigo_final) > 10):
        return 'N/A'
    
    return codigo_final



#2.2

def agregar_codigo_heroe(heroe:dict, id_heroe):
    if not heroe or type(heroe) != dict:
        return False
    
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe.get('genero', ''))
    if codigo_heroe == 'N/A' or len(codigo_heroe) != 10:
        return False

    heroe['codigo_heroe'] = codigo_heroe
    return True








#3.1

def sanitizar_entero(numero_str: str):

    numero_str = numero_str.strip()

    if not numero_str.isdigit():
        return -1
    
    try:
        numero = int(numero_str)
    except ValueError:
        return -3
    
    if numero < 0:
        return -2
    
    return numero



#3.2

def contiene_caracteres_no_numericos(cadena: str):
    for char in cadena:
        if not (char.isdigit() or char == '.'):
            return True
    
    return False

def sanitizar_flotante(numero_str: str):

    if contiene_caracteres_no_numericos(numero_str):
        return -1

    numero_str = numero_str.strip()

    try:
        numero = float(numero_str)
    except ValueError:
        return -3

    if numero < 0:
        return -2
    
    return numero




#3.3

def sanitizar_string(valor_str:str, valor_por_defecto='-'):
    
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if valor_str == '':
        return valor_por_defecto.lower()
    
    tiene_numeros = False
    for char in valor_str:
        if char.isdigit():
            tiene_numeros = True
            break
    
    if tiene_numeros:
        return 'N/A'
    
    valor_str = valor_str.replace('/', ' ')

    return valor_str.lower()



#3.4

def sanitizar_dato(heroe:dict, clave: str, tipo_dato: str):
    tipo_dato = tipo_dato.lower()
    clave = clave.lower()

    if tipo_dato not in ['string', 'entero', 'flotante']:
        print("Tipo de dato no reconocido")
        return False
    
    if clave not in heroe:
        print("La clave especificada no existe en el heroe")
        return False
    
    valor = heroe[clave]

    if tipo_dato == "string":
        heroe[clave] = sanitizar_string(valor)
    elif tipo_dato == "entero":
        heroe[clave] = sanitizar_entero(valor)
    elif tipo_dato == "flotante":
        heroe[clave] = sanitizar_flotante(valor)

    return True









#4.1


def generar_indice_nombres(lista: list):

    if not lista:
        print("El origen de datos no contiene el formato correcto")
        return

    nombres = []

    for heroe in lista:
        if not isinstance(heroe, dict) or "nombre" not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return
        
        nombre = heroe['nombre']
        palabras = nombre.split()
        nombres.extend(palabras)
    
    #print(nombres)

    return nombres


#5.1

def convertir_cm_a_mtrs(valor_cm):
    
    if isinstance(valor_cm, (int, float)) and valor_cm > 0:
        return valor_cm / 100
    else:
        return -1


#5.2

def generar_separador(patron, largo: int, imprimir: bool):

    if len(patron) < 1 or len(patron) > 2:
        return "N/A"
    
    if not isinstance(largo, int) or largo < 1 or largo > 235:
        return "N/A"
    
    separador = ''
    for h in range(largo):
        separador += patron

    if imprimir:
        print(separador)

    return separador


#5.3

def generar_encabezado(titulo:str):
    
    separador = generar_separador('*', 80, False)
    titulo = titulo.upper()

    encabezado = f"{separador}\n{titulo}\n{separador}"

    return encabezado


#5.4

def imprimir_ficha_heroe(heroe:dict):

    #encabezado principal
    encabezado_principal = generar_encabezado("Principal")

    #datos principales
    nombre = heroe.get("nombre", "")
    identidad = heroe.get("identidad", "")
    empresa = heroe.get("empresa", "")
    codigo_heroe = heroe.get("codigo_heroe", "")

    #encabezado fisico
    encabezado_fisico = generar_encabezado("Fisico")

    #datos fisicos 
    altura = convertir_cm_a_mtrs(heroe.get("altura", ""))
    peso = heroe.get("peso", "")
    fuerza = heroe.get("fuerza", "")

    #encabezado señas particulares
    encabezado_señas_particulares = generar_encabezado("Señas Particulares")


    #encabezado señas particulares
    color_ojos = heroe.get("color_ojos", "")
    color_pelo = heroe.get("color_pelo", "")

    #generar ficha
    ficha = f"{encabezado_principal}\n"
    ficha += f"NOMBRE DEL HEROE: {nombre}\n"
    ficha += f"IDENTIDAD SECRETA: {identidad}\n"
    ficha += f"CONSULTORA: {empresa}\n"
    ficha += f"CÓDIGO DE HEROE: {codigo_heroe}\n"
    ficha += f"{encabezado_fisico}\n"
    ficha += f"ALTURA: {altura} Mtrs.\n"
    ficha += f"PESO: {peso} Kg.\n"
    ficha += f"FUERZA: {fuerza} \n"
    ficha += f"{encabezado_señas_particulares}\n"
    ficha += f"COLOR DE OJOS: {color_ojos}\n"
    ficha += f"COLOR DE PELO: {color_pelo}\n"

    #imprimir
    print(ficha)


#6.1

def imprimir_menu_004():
    print("""
     --------------------------------------------------------
    |               *** STARK INDUSTRIES ***                 |
    |--------------------------------------------------------|
    |1- Imprimir la lista de nombres junto con sus iniciales |
    |2- Generar codigos de heroes                            |
    |3- Normalizar datos                                     |
    |4- Imprimir indice de nombres                           |
    |5- Navegar fichas                                       |
    |S- Salir                                                |
     --------------------------------------------------------""")









