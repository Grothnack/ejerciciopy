def es_palindromo(palabra):
    palabra = palabra.lower()  
    return palabra == palabra[::-1]

resultado = es_palindromo("radar")
print(resultado) 
