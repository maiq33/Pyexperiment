import pygame
import random

pygame.init()git status

def adivina_numero():
    # Elije un número al azar entre 1 y 100
    numero_a_adivinar = random.randint(1, 100)
    # Inicializa las variables para llevar la cuenta de las oportunidades y si se ha adivinado el número
    oportunidades = 0
    adivinado = False
    # Mientras no se haya adivinado el número y se tengan oportunidades disponibles
    while not adivinado and oportunidades < 5:
        # Pide al usuario que adivine el número
        numero_adivinado = int(input("Adivina el número entre 1 y 100: "))
        # Verifica si el número adivinado es correcto
        if numero_adivinado == numero_a_adivinar:
            print("¡Adivinaste el número! ¡Felicidades!")
            adivinado = True
        # Si el número adivinado es menor al número a adivinar
        elif numero_adivinado < numero_a_adivinar:
            print("El número es más grande.")
        # Si el número adivinado es mayor al número a adivinar
        else:
            print("El número es más pequeño.")
        oportunidades += 1
    # Si se agotaron las oportunidades y no se adivinó el número
    if not adivinado:
        print("Se te acabaron las oportunidades. El número era ", numero_a_adivinar)

adivina_numero()