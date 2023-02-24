def pu(a):
    try: 
        print (a[2]) 
    except LookupError: 
        print ("Error valor no encontrado","a[3]")
        pu(a)
    else: 
        print ("El valor se encuentra en la lista",a)
a = [1, 2, 3]
pu(a)