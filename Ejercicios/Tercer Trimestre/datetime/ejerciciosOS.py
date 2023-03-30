#------>Sistema operativo
import os

print(os.name)

#-------->Crear un directorio

import os

nombre_directorio = "mi_directorio"

try:
    os.mkdir(nombre_directorio)
    print(f"El directorio '{nombre_directorio}' ha sido creado.")
except FileExistsError:
    print(f"El directorio '{nombre_directorio}' ya existe.")

#-------> Crear un directorio recursivo en el directorio creado anteriormente

import os

ruta_directorio = "nuevo_directorio"
  
if not os.path.exists(ruta_directorio):
    os.makedirs(ruta_directorio)
    print(f"Se ha creado el directorio {ruta_directorio}")
else:
    print(f"El directorio {ruta_directorio} ya existe")

#----->crear un directorio llamado "Vocales", que tenga todas las vocales y cuando la liste aparezcan las vocales en orden

import os

vocales = ['a', 'e', 'i', 'o', 'u']
os.mkdir('Vocales')

for vocal in vocales:
    subdirectorio = os.path.join('Vocales', vocal)
    os.mkdir(subdirectorio)

contenido_directorio = os.listdir('Vocales')
vocales_ordenadas = sorted(vocales)
if contenido_directorio == vocales_ordenadas:
    print(f"Las vocales se muestran en orden: {vocales_ordenadas}")
else:
    print("No se muestran las vocales en orden.")


#--------> eliminar la carpeta "e" dentro del directorio vocales
import os

ruta = os.path.join("Vocales", "e")

try:
    os.rmdir(ruta)
    print(f"El directorio '{ruta}' ha sido eliminado.")
except OSError:
    print(f"No se pudo eliminar el directorio '{ruta}'.")
