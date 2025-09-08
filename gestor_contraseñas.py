import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("Ingrese la longitud de la contraseña: "))
password = ""
for i in range(long):
    password += random.choice(caracteres)
    print("Su contraseña es: ",password)