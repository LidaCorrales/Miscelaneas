segundos = int(input("Ingrese los segundos: "))
horas = segundos // 3600
sobrante1 = segundos % 3600
minutos = sobrante1 // 60
sobrante2 = sobrante1 % 60

print("Horas", horas)
print("Minutos", minutos)
print("Segundos", sobrante2)
