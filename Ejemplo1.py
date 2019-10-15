"""
	Ejemplo 1
	Jdesparza
"""
# Creacion de una funcion de suma
def suma(a, b):
	return a + b

# Creacion de una funcion de multiplicación
def producto(a, b):
	return a * b

# Creacion de higher-order fuctions
def disparador(f,a , b):
	print(f(a, b))
	
# para que el disparador realice las funciones dadas
disparador(producto, 1, 10)
disparador(suma, 1, 10)