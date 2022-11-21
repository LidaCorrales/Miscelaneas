"""Gaddis, T. (2015). Starting out with Python. Pearson Educación.
 https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=7498
Pagina digital: 354 - Programming Exercises"""

#Rainfall Statistics
#Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, the average monthly rainfall,
#and the months with the highest and lowest amounts
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]
variables = []
total_lluvia = 0
for i in range(12):
    variables.append(int(input("Ingresar el mes de " + str(meses[i]) + " de temporada de lluvia: ")))
    total_lluvia+=i
    print(variables)

Lluvia = variables
promedio = total_lluvia / len(variables)
print("El promedio de temporadas de lluvia fue: ", promedio)
print("Minima temporada de lluvia: " + str(min(Lluvia)))
print("Maxima temporada de lluvia" + str(max(Lluvia)))