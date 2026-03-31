Tarea 1
GIT Repo: https://github.com/eugeniogzc/compiladores-1

1. Descripción del proyecto
   Este proyecto implementa Stack (LIFO), Queue (FIFO) y Hash Table en Python, con ejemplos de uso y pruebas manuales.

Estructura del proyecto:

- src/stack.py
- src/queue.py
- src/hashtable.py
- main.py
- test.py

2. Explicación de cada estructura
   Stack (LIFO)
   Una pila donde el último elemento en entrar es el primero en salir.

- push(element): agrega al tope
- pop(): quita y regresa el tope (lanza IndexError si está vacía)
- peek(): regresa el tope sin quitarlo (lanza IndexError si está vacía)
- is_empty(): indica si está vacía
- size(): cantidad de elementos

Queue (FIFO)
Una cola donde el primero en entrar es el primero en salir.

- enqueue(element): encola al final
- dequeue(): desencola del frente (lanza IndexError si está vacía)
- front(): regresa el frente sin quitarlo (lanza IndexError si está vacía)
- is_empty(): Revisa si esta vacio
- size(): Regresa el tamaño

Hash Table (separate chaining)
Estructura que asocia key -> value usando una función hash y un arreglo de buckets.

- set(key, value): inserta o actualiza
- get(key): obtiene el valor o None si no existe
- remove(key): elimina y regresa el valor, o None si no existe
- has(key): True/False si existe la llave

3. test cases
   En test.py se prueban:

- Casos normales
  - Stack: push/pop/peek/size
  - Queue: enqueue/dequeue/front/size
  - HashTable: set/get/has/remove, overwrite de una key
- Estructuras vacías
  - Stack: pop y peek deben lanzar IndexError
  - Queue: dequeue y front deben lanzar IndexError
- Eliminación de elementos
  - HashTable: remove existente y remove inexistente
- Colisiones
  - Se buscan 2 llaves que caigan en el mismo bucket y se valida:
    - ambas se pueden obtener
    - eliminar una no rompe la otra

4. Cómo ejecutar el proyecto
   Desde el directorio raíz del proyecto:

- Ejecutar demos:
  - python main.py
- Ejecutar pruebas:
  - python test.py
