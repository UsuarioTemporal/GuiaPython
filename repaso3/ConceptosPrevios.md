## **Generadores**
Los generadores son estructuras que extraen informacion de las funciones y/o estructuras en tiempo de ejecucion , por lo que es mas eficiente que el return ,en ciertas ocaciones , esta informacion debe ser alamacenada en un objeto iterable

### **Cuando usar `yield` en lugar de `return`**
`yield` suspende la ejecución de la función y envia un valor de vuelta al emisor, pero conserva el estado suficiente , es decir tiene la capacidad de alamacenar informacion temporalmente de donde se habia quedado , para poder continuar o reaudar las instrucciones de donde se habia pausado.Cuando se quita la pausa , la funcion continua con sus intructucciones hasta volver otra ves en ese ciclo , hasta que en un cierto caso no cumpla .
Los datos enviados deben ser almacenados en un objeto iterable


```python
    #!/usr/bin/env python3
    def generador() : 
        yield 1
        yield 2
        yield 3
    
    for item in generador() : 
        print(item)
```
Salida ( Ouput terminal ) : 
> 1 <br>
> 2 <br>
> 3

Como se podra observar en la salida de los datos es consecutiva pero no recorre denuevo ta la funcion si no que se acuerda donde envio el dato y continua cumpliendo las estricciones en donde se habia quedado . **MUY INTERESANTE NO CREES :3** 

`return` devuelve un valor especificado a su interlocutor, mientras que el yield devuelve una iteracion de valores. Se deberia usar el `yield` cuando queremos iterar sobre una secuencia , pero no queremos alamacenar toda la secuencia en la memoria .

**EJM**

```python
    #!/usr/bin/env python3


```

## **Decoradores**




[**MAS INFORMACIÓN SOBRE GENERADORES**](https://www.geeksforgeeks.org/generators-in-python/)

[**MAS INFORMACIÓN SOBRE DECORADORES**](https://www.geeksforgeeks.org/decorators-in-python/)