"""
	Ejemplo 3
	Jdesparza
"""
# se crea una lista
datos = [1, 2, 10, 11, 12, 13]
# variable con una operacion
resultado = filter(lambda x: x % 2 == 0, datos)
# se imprime los resultados
print(resultado)
print(list(resultado))