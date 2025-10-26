import sys

try:
    print("Hello my name is", sys.argv[1])
    # Se usa el index 1 ya que el argumento en el index 1 es el nombre del programa
except IndexError:
    # print("Hola"[1:-1])
    sys.exit("You have to enter your name...")




