#ImportError importa un modulo q no existe 

lista2=[2,3,4,5,6,78,9]
def PromedioLista(lista2):
        try:
            cantidad_elementos = len(lista2)
            suma2 = 0
            for valor in lista2:
            suma2 = suma2 + valor
                promedio = suma2 / cantidad_elementos
            return promedio
        except IndentationError:
             print("coloca bien la identacion")
        except:
             print("otro error")

print(PromedioLista(lista2))
