"""
	Ejemplo 2
	Jdesparza
"""
# se crea una lista
datos = [1, 2, 10, 11, 12, 13]

# para ir guardando en un tipo de lista los resultados
resultado = []

# para recorrer toda la lista
for i in datos:
	if i%2==0: # para determinar cuales son pares
		# para guardar los pares en una lista
		resultado.append(i)
		
# Se imprime una lista con los números pares
print(resultado)