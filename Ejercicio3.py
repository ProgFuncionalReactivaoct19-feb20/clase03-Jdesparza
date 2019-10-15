"""
	Ejemplo 7
	Jdesparza

	Funcional - Aplicando función filter

	Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.

	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
"""
# se crea una lista con las ciudades
ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]
# variable que filtra mediante el uso de lambda aquellas ciudades que tienen un caracter par
resultado = filter(lambda x: len(x) % 2 == 0, ciudades)
# se imprime los resultados
print(resultado)
print(list(resultado))
