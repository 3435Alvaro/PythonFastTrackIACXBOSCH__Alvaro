# PEP 8

1. Sangría y espacios en blanco:
   - Regla: Utilizar una sangría de 4 espacios para indicar bloques de código anidados. Utilizar espacios alrededor de operadores y después de comas.
   ```python
   def mi_funcion():
       if condicion:
           print("Bloque anidado")
   ```

2. Longitud de línea:
   - Regla: Limitar la longitud de línea a 79 caracteres.
   ```python
   resultado = variable1 + variable2 + variable3 + variable4
   ```

3. Nombres de variables y funciones:
   - Regla: Utilizar nombres en minúsculas para variables y funciones, y separar palabras con guiones bajos.
   ```python
   mi_variable = 10
   ```

4. Nombres de constantes:
   - Regla: Utilizar nombres en mayúsculas para constantes.
   ```python
   PI = 3.1416
   ```

5. Comentarios:
   - Regla: Utilizar comentarios para explicar el propósito del código y aclarar secciones difíciles de entender.
   ```python
   # Calcula el área de un círculo
   area = pi * radio ** 2
   ```

6. Importaciones:
   - Regla: Organizar las importaciones en grupos, separadas por una línea en blanco.
   ```python
   import os
   import numpy as np
   from mi_modulo import funcion1, funcion2
   ```

7. Convención de nombres:
   - Regla: Utilizar guiones bajos para separar palabras en nombres de variables, funciones y métodos.
   ```python
   nombre_completo = "John Doe"
   ```

8. Clases y métodos:
   - Regla: Utilizar nombres en CamelCase para clases y nombres en minúsculas con guiones bajos para métodos.
   ```python
   class MiClase:
       def mi_metodo(self):
           pass
   ```

9. Uso de espacios alrededor de operadores:
   - Regla: Utilizar espacios alrededor de operadores para mejorar la legibilidad.
   ```python
   resultado = 10 * (2 + 3)
   ```

10. Orden de importaciones:
    - Regla: Ordenar las importaciones de forma ascendente, primero las bibliotecas estándar, seguidas de bibliotecas de terceros y, por último, las importaciones locales.
    ```python
    import os
    import sys
    import numpy as np
    import mi_modulo
    ```

Estos ejemplos ilustran cómo se aplica cada regla de PEP-8 en el código Python. Al seguir estas reglas, lograrás un estilo de código más consistente y legible, lo cual facilita la colaboración y el mantenimiento del código a largo plazo.