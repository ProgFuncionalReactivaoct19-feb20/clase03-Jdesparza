"""
	Ejemplo 6
	Jdesparza

	Funcional - Aplicando función filter

	Dado un conjunto de palabras filtrar todas aquellas que sean palindromas:
	"oro", "pais", "ojo", "oso", "radar", "sol", "seres"
"""
# se crea una lista
datos = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
# para filtrar los resultados luego de hacer una operacion con lambda
resultado = filter(lambda x: x == "".join(reversed(x)), datos)

# se imprime los resultados
print(resultado)
print(list(resultado))