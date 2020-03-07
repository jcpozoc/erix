def validarNumero(prompt,min,max):
    while (True):
        try:
            x=int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Ingresar solo números")
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")

v = validarNumero("Ingrese un valor dentro de -10 a 10:   30",-10,10)

print ("El número es:", v)
    
