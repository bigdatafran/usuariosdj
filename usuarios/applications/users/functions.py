# Funciones extra de la aplicación users
# 
import random
import string

def code_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    # Esta funnción genera un string o código de 6 dígitos que puede incluir número y letras
    return ''.join(random.choice(chars)  for _ in range(size))
