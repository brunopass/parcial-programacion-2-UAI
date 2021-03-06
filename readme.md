# Parcial - Passarelli Bruno
![uai](https://ccdfit.com/wp-content/uploads/2019/12/Universidad-Abierta-Interamericana-UAI-01.png)
## preguntas馃摑

#### 1. Indique tres diferencias sustanciales al momento de dise帽ar un programa utilizando el paradigma estructurado y paradigma orientado a objetos. (10)
```txt
    - reutilizaci贸n
    - abstracci贸n
    - subtipificaci贸n
```

#### 2. 驴Por qu茅 decimos que python es un lenguaje semi-interpretado y con tipado din谩mico? (10)
```txt
    decimos que python es un lenguaje semi interpretado, ya que primero, el script python se traduce a bytecode que posee la extensi贸n .pyc o .pyo
    para luego ser interpretado.
    el tipado din谩mico se refiere a que no es necesario declarar el tipo de dato que va a ser contenido en una variable
```

#### 3. 驴Qu茅 estructuras condicionales permite el lenguaje python? Ejemplifique con una porci贸n de c贸digo. (10)
```py
    podemos utilizar:

    operadores relacionales:

    == Es igual
    != Es diferente
    > Es mayor
    >= Es mayor o igual
    < Es menor
    <= Es menor o igual

    operadores l贸gicos:

    and
    or
    not

    # ejemplo 1:
    condicion1 = True
    condicion2 = False
    if condicion1 and condicion2:
        # ...
    else:
        # ...

    value1 = 0
    
    if value1 > 10:
        #...
    elif value1 >0 and value1 < 10:
        #...
    else:
        #...

    # ejemplo 3:
    conditions = ["value1", "value2"]
    if "value1" in conditions:
        # ...
    
```

#### 4. 驴Qu茅 estructuras repetitivas permite el lenguaje python? Ejemplifique con una porci贸n de c贸digo. (10)
```py
    tenemos 2 for y while

    # ejemplo for:
    for i in range(10):
        print(i)

    # ejemplo while:
    condition = True
    while condition:
        print("condition is true")
    
```

#### 5. 驴Cu谩les son las diferencias entre listas, tuplas y diccionarios en python? (10)
```py
    - las LISTAS (List) son arrays mutables.
    
    - las TUPLAS (tuple) son arrays inmutables.

    - los DICCIONARIOS (TypedDict) son estructuras de datos de tipo key-value
```

#### 6. 驴C贸mo se declara una clase? Ejemplifique (10)
```py
    utilizando la palabra reservada class

    ejemplo:

    class Objeto:
        # ...
```

#### 7. 驴C贸mo declaro una propiedad? Ejemplifique (10)
```py
    en python todas las propiedades de una clase son p煤blicas,
    sin embargo existe un standard el cual define a las propiedades
    que empiecen con __ como 'privadas'.
    para agregar una propiedad solo hay que escribirla dentro de la clase como
    una variable m谩s.

    ejemplo:

    class Objeto:
        prop_publica
        __prop_privada
```

#### 8. 驴Qu茅 es el Duck typing? (10)
```txt
    El duck typing es la forma de progamar donde identificamos a nuestros elementos 
    dependiendo de los m茅todos y atributos que contengan.
```

#### 9. Ejemplifique c贸mo se puede implementar polimorfismo con python (10)
```py
    class Forma:
        def dibujar(self):
            print('dibujar')

    class Cuadrado(Forma):
        def dibujar(self):
            print('dibujar cuadrado')

    class Circulo(Forma):
        def dibujar(self):
            print('dibujar circulo')

```

#### 10. 驴Cu谩l es la diferencia entre los m茅todos init y new? (10)
```py
    el m茅todo __init__ crea el objeto y luego lo inicializa, no es el constructor como tal, en cambio el m茅todo __new__ s贸lo construye el objeto.
```

## Pr谩ctica馃捇

### run docker
```bash
    docker build -t parcial-bruno-passarelli .
    docker run -it parcial-bruno-passarelli
```