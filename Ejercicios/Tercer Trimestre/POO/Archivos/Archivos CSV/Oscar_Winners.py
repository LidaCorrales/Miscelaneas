"""import csv
listadeGanadores=[]
with open('E:\\Miscelaneas_LidaCorrales\\Ejercicios\\Tercer Trimestre\\POO\\Archivos\\Archivos CSV\\oscar_age_everybody.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('Index:',row[0])
        print('Year:',row[1])
        print('Age:',row[2])
        print('Name:',row[3])
        print('Movie:',row[4])"""
        
from Ganadores import *
import csv
listadeGanadores=[]
with open('E:\\Miscelaneas_LidaCorrales\\Ejercicios\\Tercer Trimestre\\POO\\Archivos\\Archivos CSV\\oscar_age_everybody.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=Ganadores(row[0],row[1],row[2],row[3],row[4])
        listadeGanadores.append(ob)      
#print(listadeGanadores)
for aprendiz in listadeGanadores:
    print(Ganadores.nombrePelicula())
print(listadeGanadores)