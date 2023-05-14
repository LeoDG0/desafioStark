
from data_stark import lista_personajes
import os
from funciones import *

personaje_alto = lista_personajes[0]
personaje_bajo = lista_personajes[0]


flagLista = False
flagAlturas = False

lista = []

cargarLista(lista, lista_personajes)

while True:
    os.system("cls")
    match(menu()):
        case 1:
            mostrarPersonas(lista)
            flagLista = True

        case 2:
            if (flagLista != False):
                mostrarPersonasAlturas(lista)
            else:
                print("Primero debe cargar la lista!")
        case 3:
            if (flagLista != False):
                personaje_alto = personajeAlto(lista)
            else:
                print("Primero debe cargar la lista!")
        case 4:
            if (flagLista != False):
                personaje_bajo = personajeBajo(lista)
                flagAlturas = True
            else:
                print("Primero debe cargar la lista!")
        case 5:
            if (flagLista != False):
                calcularPromedio(lista)
            else:
                print("Primero debe cargar la lista!")
        case 6:
            if (flagLista != False):
                if (flagAlturas != False):
                    mostrarNombres("alto","bajo",personaje_alto, personaje_bajo, "altura", "altura")
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
            if (salir == "s"):
                break
    os.system("pause")
