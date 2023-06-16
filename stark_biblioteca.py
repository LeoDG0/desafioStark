from funciones import *
from data_stark import lista_personajes
import os


def stark_normalizar_datos_002(lista: list):

    if not lista:
        print("Error: lista vacia!")
        return
    
    keys_numericas = ["altura", "peso", "fuerza"]

    datos_modificacos = False

    for heroe in lista:
        for key, valor in heroe.items():
            if(key in keys_numericas):
                #valido que el dato sea diferente al que se va a castear
                if(isinstance(valor, str)):
                    try:
                        #intento castear
                        heroe[key] = int(valor)
                    
                    except ValueError:
                        try:
                            heroe[key] = float(valor)
                        except ValueError:
                            pass #no pude castear no hago nada
            elif(isinstance(valor, float) and key != "peso"):
                heroe[key] = int(valor)
                datos_modificacos = True

    if(datos_modificacos):
        print("Datos normalizados")


def stark_imprimir_nombres_heroes(lista: list):
    
    if not lista:
        print("Error: Lista de heroes vacia")
        return -1
    
    for heroe in lista:
        nombre_normalizado = obtener_nombre(heroe)
        imprimir_dato(nombre_normalizado)


def stark_imprimir_nombres_alturas(lista: list):

    if not lista:
        return -1
    
    for heroe in lista:
        nombre_altura = obtener_nombre_y_dato(heroe, "altura")
        imprimir_dato(nombre_altura)


def stark_calcular_imprimir_heroe(lista: list, maximo_minimo, key):

    if not lista:
        return -1
    
    heroe = calcular_max_min_dato(lista, maximo_minimo, key)

    if heroe is not None:
        if(maximo_minimo == "maximo"):
            dato_formateado = obtener_nombre_y_dato(heroe, key)
            print("MAYOR ALTURA: ", end="")
            imprimir_dato(dato_formateado)
        elif(maximo_minimo == "minimo"):
            dato_formateado = obtener_nombre_y_dato(heroe, key)
            print("MENOR ALTURA: ", end="") 
            imprimir_dato(dato_formateado)
    else:
        print("Error: No se a podido buscar el heroe!")




def stark_calcular_imprimir_promedio_altura(lista: list, key:str):

    if not lista:
        return -1

    promedio_altura = calcular_promedio(lista, key)

    print("El promedio de altura es ", end="")
    imprimir_dato(str(promedio_altura))





def stark_menu_principal_02():
    imprimir_menu_002()
    opcion = input("Ingrese opcion: ")
    if(validar_entero(opcion) == True):
        opcion = int(opcion)
        return opcion
    else:
        print("Debe ingresar una opcion correcta!")
        return -1


#7
import pdb

def stark_marvel_app(lista_p: list):

    flagLista = False
    flagAlturas = False
    salir = 'n'
    lista = []
    cargarLista(lista, lista_p)
    stark_normalizar_datos_002(lista)

    while salir == 'n':
        os.system("cls")
        
        match(stark_menu_principal_02()):
            case 1:
                stark_imprimir_nombres_heroes(lista)
                flagLista = True
            case 2:
                if (flagLista != False):
                    stark_imprimir_nombres_alturas(lista)
                else:
                    print("Primero debe cargar la lista!")
            case 3:
                if (flagLista != False):
                    stark_calcular_imprimir_heroe(lista, "maximo", "altura")
                else:
                    print("Primero debe cargar la lista!")
            case 4:
                if (flagLista != False):
                    stark_calcular_imprimir_heroe(lista, "minimo", "altura")
                    flagAlturas = True
                else:
                    print("Primero debe cargar la lista!")
            case 5:
                if (flagLista != False):
                    stark_calcular_imprimir_promedio_altura(lista, "altura")
                else:
                    print("Primero debe cargar la lista!")
            case 6:
                if (flagLista != False):
                    if (flagAlturas != False):
                        stark_calcular_imprimir_heroe(lista, "maximo", "altura")
                        stark_calcular_imprimir_heroe(lista, "minimo", "altura")
                    else:
                        print("Primero debe determinar las alturas con las opciones 3 y 4!")
                else:
                    print("Primero debe cargar la lista y luego determinar las alturas!")
            case 7:
                if (flagLista != False):
                    filtrar_pesos(lista)
                else:
                    print("Primero debe cargar la lista!")
            case 8:
                if (flagLista != False):
                    submenu2(lista)
                else:
                    print("\nPrimero debe cargar la lista para desbloquear las demas opciones!\n")
            case 9:
                salir = input("Confirma salida? s/n: ")
                if (salir.lower() == "s"):
                    break
                elif(salir.lower() == "n"):
                    print("Cancelando salida!")
                else:
                    print("Ingreso una opcion invalida!")
        os.system("pause")





def stark_imprimir_nombres_con_iniciales(lista: list):
    
    if (type(lista) != list or len(lista) == 0):
        return
    
    if agregar_iniciales_nombre(lista):
        for heroe in lista:
            nombre = heroe["nombre"]
            iniciales = heroe["iniciales"]
            print("* {} ({})".format(nombre, iniciales))



def stark_generar_codigos_heroes(lista: list):

    if not lista or type(lista) != list:
        print("El origen de datos no contiene el formato correcto")
        return
    
    for i in range(len(lista)):
        heroe = lista[i]
        if type(heroe) != dict or 'genero' not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return
        agregar_codigo_heroe(heroe, i)

    print(f"Se asignaron {len(lista)} codigos")
    print(f"El codigo del primer heroe es: {lista[0]['codigo_heroe']}")
    print(f"El codigo del ultimo heroe es: {lista[-1]['codigo_heroe']}")




def stark_normalizar_datos_004(lista: list):

    if not lista:
        print("Error: Lista de heroes vacia")
        return

    for heroe in lista:
        sanitizar_dato(heroe, 'altura', 'flotante')
        sanitizar_dato(heroe, 'peso', 'flotante')
        sanitizar_dato(heroe, 'color_ojos', 'string')
        sanitizar_dato(heroe, 'color_pelo', 'string')
        sanitizar_dato(heroe, 'fuerza', 'entero')
        sanitizar_dato(heroe, 'inteligencia', 'entero')

    print("Datos normalizados")



def stark_imprimir_indice_nombres(lista: list):

    indice_nombres = generar_indice_nombres(lista)
    if indice_nombres:
        indice_str = '-'.join(indice_nombres)
        print(indice_str)
    else:
        print("El origen de datos no contiene el formato correcto")




def stark_navegar_fichas(lista: list):

    if len(lista) == 0:
        print("Error: Lista de heroes vacia")
        return
    
    indice_actual = 0
    salir = False

    while not salir:
        heroe_actual = lista[indice_actual]
        os.system("cls")
        imprimir_ficha_heroe(heroe_actual)

        opcion = input("[1] Ir a la izquierda  [2] Ir a la derecha  [S] Salir: ")
        if opcion == '1':
            indice_actual = (indice_actual - 1) % len(lista)
        elif opcion == '2':
            indice_actual = (indice_actual + 1) % len(lista)
        elif opcion.upper() == 'S':
            salir = True
        else:
            print("Opcion no valida. Intente nuevamente.")




def stark_menu_principal_04():

    imprimir_menu_004()
    try:
        opcion = input("Ingrese una opcion: ")
        return opcion.upper()
    except ValueError:
        print("Debe ingresar una opcion correcta!")
    
    return -1



#6.3

def stark_marvel_app_4(lista_p: list):
    salir = 'n'
    lista = []
    cargarLista(lista, lista_p)

    while salir == 'n':
        os.system("cls")
        opcion = stark_menu_principal_04()
        if opcion == '1':
            stark_imprimir_nombres_con_iniciales(lista)
        elif opcion == '2':
            stark_generar_codigos_heroes(lista)
        elif opcion == '3':
            stark_normalizar_datos_004(lista)
        elif opcion == '4':
            stark_imprimir_indice_nombres(lista)
        elif opcion == '5':
            stark_navegar_fichas(lista)
        elif opcion == 'S':
            salir = input("Confirma salida? s/n: ")
            if salir.lower() == "s":
                break
            elif salir.lower() == "n":
                print("Cancelando salida!")
            else:
                print("Ingreso una opcion invalida!")
        else:
            print("Opción inválida")
        os.system("pause")









