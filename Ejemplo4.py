"""
	Ejemplo 4
	Jdesparza
"""
# se crea una lista
datos = [18, 19, 20, 10, 11, 12]
# variable con una operacion
resultado = filter(lambda x: x >= 18 or x <= 10, datos)
# se imprime los resultados
print(resultado)
print(list(resultado))