# Parcial - Passarelli Bruno
![uai](https://ccdfit.com/wp-content/uploads/2019/12/Universidad-Abierta-Interamericana-UAI-01.png)
## preguntas📝

#### 1. Indique tres diferencias sustanciales al momento de diseñar un programa utilizando el paradigma estructurado y paradigma orientado a objetos. (10)
```txt
    - reutilización
    - abstracción
    - subtipificación
```

#### 2. ¿Por qué decimos que python es un lenguaje semi-interpretado y con tipado dinámico? (10)
```txt
    decimos que python es un lenguaje semi interpretado, ya que primero, el script python se traduce a bytecode que posee la extensión .pyc o .pyo
    para luego ser interpretado.
    el tipado dinámico se refiere a que no es necesario declarar el tipo de dato que va a ser contenido en una variable
```

#### 3. ¿Qué estructuras condicionales permite el lenguaje python? Ejemplifique con una porción de código. (10)
```py
    podemos utilizar:

    operadores relacionales:

    == Es igual
    != Es diferente
    > Es mayor
    >= Es mayor o igual
    < Es menor
    <= Es menor o igual

    operadores lógicos:

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

#### 4. ¿Qué estructuras repetitivas permite el lenguaje python? Ejemplifique con una porción de código. (10)
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

#### 5. ¿Cuáles son las diferencias entre listas, tuplas y diccionarios en python? (10)
```py
    - las LISTAS (List) son arrays mutables.
    
    - las TUPLAS (tuple) son arrays inmutables.

    - los DICCIONARIOS (TypedDict) son estructuras de datos de tipo key-value
```

#### 6. ¿Cómo se declara una clase? Ejemplifique (10)
```py
    utilizando la palabra reservada class

    ejemplo:

    class Objeto:
        # ...
```

#### 7. ¿Cómo declaro una propiedad? Ejemplifique (10)
```py
    en python todas las propiedades de una clase son públicas,
    sin embargo existe un standard el cual define a las propiedades
    que empiecen con __ como 'privadas'.
    para agregar una propiedad solo hay que escribirla dentro de la clase como
    una variable más.

    ejemplo:

    class Objeto:
        prop_publica
        __prop_privada
```

#### 8. ¿Qué es el Duck typing? (10)
```txt
    El duck typing es la forma de progamar donde identificamos a nuestros elementos 
    dependiendo de los métodos y atributos que contengan.
```

#### 9. Ejemplifique cómo se puede implementar polimorfismo con python (10)
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

#### 10. ¿Cuál es la diferencia entre los métodos init y new? (10)
```py
    el método __init__ crea el objeto y luego lo inicializa, no es el constructor como tal, en cambio el método __new__ sólo construye el objeto.
```

## Práctica💻

### run docker
```bash
    docker build -t parcial-bruno-passarelli .
    docker run -it parcial-bruno-passarelli
```