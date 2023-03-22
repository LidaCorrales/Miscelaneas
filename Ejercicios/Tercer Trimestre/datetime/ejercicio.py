#Usa la clase datetime para mantener los valores que consisten en componentes fechas y componentes de tiempo.
#Al igual que con date, hay varios métodos de clase convenientes para crear instancias datetime de otros
# valores comunes.

import datetime

print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
print()

FIELDS = [
    'year', 'month', 'day',
    'hour', 'minute', 'second',
    'microsecond',
]

d = datetime.datetime.now()
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(d, attr)))


#La instancia datetime tiene todos los atributos de un objeto date y un objeto time.