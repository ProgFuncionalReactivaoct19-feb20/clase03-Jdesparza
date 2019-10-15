"""
	Ejemplo 7
	Jdesparza

	Funcional - Aplicando función filter

	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

	Loja, Pichincha, Esmeraldas, Azuay, Imbabura

	Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
"""
# creación de una función
def es_placa(x):
	# se crea una lista para determinar las placas de las provincias dadas
	l_placas = ["l", "p", "e", "a", "i"]
	# para detreminar si las placas pertenecen a las provincias
	if x[0] in l_placas:
		# retorna verdadero en el caso de que si sea
		return True
	else:
		# retorna falso en el caso de que no sea
		return False

# se crea una lista tipo String
placas = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]

# variable que opera con filter para recorrer y buscar las placas pertenecen
resultado = filter(es_placa, placas)
# se imprime los resultados
print(resultado)
print(list(resultado))
