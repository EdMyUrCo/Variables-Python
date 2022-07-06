#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, 
# guarda el resultado en una variable

nombre = input("Digite nombre: ")
apellido = input("Digite apellido: ")

print("Hola,", nombre, apellido + ", Bienvenid@")

#Investiga sobre el límite de los enteros y los flotantes en python 
# y anotar sus descubrimientos como comentarios en el archivo

#INT
"""
Los tipos enteros o int en Python permiten almacenar un valor numérico no decimal 
ya sea positivo o negativo de cualquier valor. 
 
Si por ejemplo se usan enteros de 32 bits el rango a representar es de -2^31 a 2^31–1, 
es decir, -2.147.483.648 a 2.147.483.647. Con 64 bits, 
el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807.
"""

#FLOAT
"""
El módulo decimal proporciona soporte para aritmética decimal de coma flotante rápida y con redondeo matemáticamente correcto. Ofrece varias ventajas en comparación con el tipo de dato float:

+ Decimal «se basa en un modelo de coma flotante que se diseñó pensando en las personas, y necesariamente tiene un principio rector supremo: las computadoras deben proporcionar una aritmética que funcione de la misma manera que la aritmética que las personas aprenden en la escuela.» – extracto (traducido) de la especificación de la aritmética decimal.

+ Los números decimales se pueden representar de forma exacta en coma flotante decimal. En cambio, números como 1.1 y 2.2 no tienen representaciones exactas en coma flotante binaria. Los usuarios finales normalmente no esperaran que 1.1 + 2.2 se muestre como 3.3000000000000003, como ocurre al usar la representación binaria en coma flotante.

+ La exactitud se traslada a la aritmética. En coma flotante decimal, 0.1 + 0.1 + 0.1 - 0.3 es exactamente igual a cero. En coma flotante binaria, el resultado es 5.5511151231257827e-017. Aunque cercanas a cero, las diferencias impiden pruebas de igualdad confiables y las diferencias pueden acumularse. Por estas razones, se recomienda el uso de decimal en aplicaciones de contabilidad con estrictas restricciones de confiabilidad.

+ El módulo decimal incorpora una noción de dígitos significativos, de modo que 1.30 + 1.20 es 2.50. El cero final se mantiene para indicar el número de dígitos significativos. Esta es la representación habitual en aplicaciones monetarias. Para la multiplicación, el método de «libro escolar» utilizado usa todas las cifras de los multiplicandos. Por ejemplo, 1.3 * 1.2 es igual a 1.56, mientras que 1.30 * 1.20 es igual a 1.5600.
"""

#Aplica la fórmula de la suma de los primeros n números pares
#(investigar), tomando como n la variable de tipo entero y 
# almacenar el resultado en una variable

"""
SUMA DE LOS PRIMEROS NÚMEROS CONSECUTIVOS:
"""
n = 1
sumaNum = ((n * ( n + 1 ))/2)

"""
SUMA DE LOS PRIMEROS NÚMEROS PARES:
"""

sumaPar = (n * ( n + 1 ))

"""
SUMA DE LOS PRIMEROS NÚMEROS IMPARES
"""

sumaImpar = n * n

#Imprimir los resultados de las tareas anteriores

"""
SUMA DE LOS PRIMEROS NÚMEROS CONSECUTIVOS:
"""
print(f"La suma de los primeros números consecutivos {sumaNum}")

"""
SUMA DE LOS PRIMEROS NÚMEROS PARES:
"""
print("La suma de los primeros números pares:", sumaPar)

"""
SUMA DE LOS PRIMEROS NÚMEROS IMPARES
"""

print("La suma de los primeros números impares: " + sumaImpar)
