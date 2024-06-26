def devolver_distintos(a, b, c):
    suma = a + b + c
    
    if suma > 15:
        resultado = max(a, b, c)
    elif suma < 10:
        resultado = min(a, b, c)
    else:
        resultado= a + b + c -max(a, b, c) + min(a, b, c)
           
        return resultado
    
    print(resultado)
