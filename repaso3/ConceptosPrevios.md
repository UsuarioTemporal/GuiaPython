## **Generadores**
Los generadores son estructuras que extraen informacion de las funciones y/o estructuras en tiempo de ejecucion , por lo que es mas eficiente que el return ,en ciertas ocaciones , esta informacion debe ser alamacenada en un objeto iterable

### **Cuando usar `yield` en lugar de `return`**
`yield` suspende la ejecución de la función y envia un valor de vuelta al emisor, pero conserva el estado suficiente , es decir tiene la capacidad de alamacenar informacion temporalmente de donde se habia quedado , para poder continuar o reaudar las instrucciones de donde se habia pausado.Cuando se quita la pausa , la funcion continua con sus intructucciones hasta volver otra ves en ese ciclo , hasta que en un cierto caso no cumpla .
Los datos enviados deben ser almacenados en un objeto iterable


```python
    def generador() : 
        yield 1
        yield 2
        yield 3
    
    for item in generador() : 
        print(item)
```
Salida : 
> 1 <br>
> 2 <br>
> 3


## **Decoradores**




[**MAS INFORMACIÓN SOBRE GENERADORES**](https://www.geeksforgeeks.org/generators-in-python/)

[**MAS INFORMACIÓN SOBRE DECORADORES**](https://www.geeksforgeeks.org/decorators-in-python/)