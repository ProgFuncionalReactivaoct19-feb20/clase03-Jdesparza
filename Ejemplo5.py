"""
	Ejemplo 5
	Jdesparza

	Funcional - Aplicando función filter
"""
# creación de una función
def es_vocal(x):
	# se crea una lista con las vocales
	vocales = ["a", "e", "i", "o", "u"]
	# para detreminar si el dato es una vocal
	if x in vocales:
		# retorna verdadero en el caso de que si sea
		return True
	else:
		# retorna falso en el caso de que no sea
		return False
# se crea una lista tipo String
datos = ["e", "c", "u", "a", "d", "o", "r"]
# variable que opera para determinar si los datos son vocales
resultado = filter(es_vocal, datos)
# se imprime los resultados
print(resultado)
print(list(resultado))
