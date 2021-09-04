#!/usr/bin/env python
# coding: utf-8

# <img src="Archivos/miad4.png" width=800x>
# 
# # Funciones
# 
# En este taller usarás funciones y funciones anónimas para resolver diversos problemas.
# 
# ## Habilidades en práctica
# Al desarrollar este taller podrás verificar tu progreso para:
# 
# **1.** Implementar funciones e integrarlas con condicionales y ciclos. <br>
# **2.** Implementar funciones anónimas e integrarlas con condicionales.
# 
# ## Instrucciones
# En cada uno de los siguientes ejercicios deberás escribir el código solicitado estrictamente en las celdas indicadas para ello, teniendo en cuenta las siguientes recomendaciones:
# 
# * No crear, eliminar o modificar celdas de este Notebook (salvo lo que se te indique), pues puede verse afectado el proceso de calificación automática.
# * La calificación se realiza de manera automática con datos diferentes a los proporcionados en este taller. Por consiguiente, tu código debe funcionar para diferentes instancias de cada uno de los ejercicios; una instancia hace referencia al valor de los parámetros.
# * La calificación de cada ejercicio depende del valor que retorne la función especificada en su enunciado. Por lo tanto, aunque implementes funciones adicionales, es escencial que utilices los nombres propuestos en los enunciados de los ejercicios para implementar la función definitiva.
# 
# Esta es una actividad calificada y, por lo tanto, debe ser resuelta individualmente.
# 
# A continuación puedes ver un ejemplo de los ejercicios que encontrarás en este taller.

# ### Ejemplo
# 
# Implementa una función llamada `multiplicacion` que reciba dos números ingresados por parámetro y retorne la multiplicación de estos dos.
# 
# *Esta función debería retornar un número*

# In[1]:


# Implementa tu respuesta en esta celda

def multiplicacion(num1, num2):
    
    respuesta = num1 * num2
    
    return respuesta


# ### Ejercicio 1
# 
# A continuación, encuentras declarada una lista de números.

# In[2]:


# No modifiques esta celda

lista = [20, 12, 21.3, 34]


# Implementa una función llamada `suma_lista` que reciba por parámetro una lista de números (por ejemplo, la variable `lista`) y retorne la suma de todos sus elementos.
# 
# *Esta función debe retornar un número*.

# In[3]:


# YOUR CODE HERE

def suma_lista(lista):
    suma_elementos= 0 
    for i in range(len(lista)):
        suma_elementos += lista[i]
    return suma_elementos
    
#raise NotImplementedError()


# In[4]:


## AUTO-CALIFICADOR

# Base variables
lista = [20, 12, 21.3, 34]
lista_prueba = [23.7, 15.1, 22.2, 21, 16.1, 24, 15.9]

# Caso 1: no existe la función.
try:
    suma_lista
    assert type(suma_lista) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada suma_lista.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    suma_lista(lista)
    suma_lista(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna un número
assert type(suma_lista(lista_prueba)) == float, f"Tu función debe retornar un valor de tipo {float.__name__}."

# Caso 4: respuesta explicita
assert suma_lista(lista_prueba) != 87.3, "Tu respuesta es incorrecta para una instancia diferente. Utiliza el parámetro."

# Caso 5: suma elemento por elemento
assert suma_lista(lista_prueba) >= 138.0, "Tu función puede no estar sumando todos los elementos de la lista."

# Caso 6: retorna un numero distinto del esperado
assert suma_lista(lista_prueba) == 138.0, "Tu función no retorna el valor correcto."
assert suma_lista(lista) == 87.3, "Tu función no retorna el valor correcto."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 2
# 
# A continuación, encuentras declarada una lista que contiene letras y números.

# In[5]:


lista = [23, "2", 46 , "l", 8.3, "m"]


# Implementa una función llamada `primera_letra` que reciba una lista de números y letras por parámetro (por ejemplo, la variable `lista`), y retorne el primer elemento que sea una letra. La función debe retornar una cadena de texto vacía (`""`) si no encuentra una letra.
# 
# *Esta función debe retornar una letra*.

# In[6]:


# YOUR CODE HERE
alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
lista_prueba = [23.7, "15", "22.2", 21, 48, "x", 24, 15.9, "f"]
lista_prueba_2 = [23.7, "15", "22.2", 21, "x", 24, 15.9, "f"]
lista_prueba_3 = [23.7, "15", "22.2", 21, 24, 15.9]

def primera_letra(lista):
    elemento = ""
    i=0
    while elemento == "":
        if i<=len(lista):
            if lista[i] in alfabeto:
                elemento = lista[i]
            else:
                i += 1
        else:
            pass
    return elemento
     
ejercicio = primera_letra(lista_prueba_2)
ejercicio
#raise NotImplementedError()


# In[7]:


## AUTO-CALIFICADOR

# Base variables
lista = [23, "2", 46 , "l", 8.3, "m"]
lista_prueba = [23.7, "15", "22.2", 21, 48, "x", 24, 15.9, "f"]
lista_prueba_2 = [23.7, "15", "22.2", 21, "x", 24, 15.9, "f"]
lista_prueba_3 = [23.7, "15", "22.2", 21, 24, 15.9]

# Caso 1: no existe la función.
try:
    primera_letra
    assert type(primera_letra) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada primera_letra.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    primera_letra(lista)
    primera_letra(lista_prueba)
    primera_letra(lista_prueba_2)
    primera_letra(lista_prueba_3)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: no retorna una letra
assert type(primera_letra(lista_prueba)) == str, f"Tu función debe retornar un valor de tipo {str.__name__}."

# Caso 4: respuesta explicita
assert primera_letra(lista_prueba) != "l", "Tu respuesta es incorrecta para para una instancia diferente. Utiliza el parámetro."

# Caso 5: la función retorna vacio
assert primera_letra(lista_prueba_3) == "", "Tu función debe retornar una cadena de texto vacía cuando no hay una letra en la lista."

# Caso 6: no encuentra letras.
assert primera_letra(lista_prueba) != "", "Tu función no encuentra una letra en la lista. Puede no estar explorando todos sus elementos."

# Caso 7: retorna una letra distinta de la esperada
assert primera_letra(lista_prueba) == "x", "Tu función no retorna la letra correcta."
assert primera_letra(lista) == "l", "Tu función no retorna la letra correcta."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 3
# 
# A continuación, encuentras declarada una lista que contiene letras y números.

# In[8]:


lista = [4, 3, 8, 5, 6, 2, 7, 5]


# Implementa una función llamada `separar_pares_impares` que reciba una lista de números enteros por parámetro (por ejemplo, la variable `lista`) y retorne una tupla que contenga dos listas, cada una ordenada ascendentemente:
# 
# * La primera lista debe contener los números pares.
# * La segunda lista debe contener los números impares.
# 
# *Esta función debe retornar una tupla de listas*.

# In[16]:


# YOUR CODE HERE
def separar_pares_impares(lista):
    lista_pares =[]
    lista_impares = []
    
    for i in range(len(lista)):
        if lista[i] %2 ==0:
            lista_pares.append(lista[i])
        else:
            lista_impares.append(lista[i])
    
    lista_pares.sort()
    lista_impares.sort()
    return lista_pares,lista_impares



#raise NotImplementedError()


# In[17]:




# Base variables
lista = [4, 3, 8, 5, 6, 2, 7, 5]
lista_prueba = [3, 1, 2, 8, 6, 6, 7, 10, 9, 8]

# Caso 1: no existe la función.
try:
    separar_pares_impares
    assert type(separar_pares_impares) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada separar_pares_impares.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    separar_pares_impares(lista)
    separar_pares_impares(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna una tupla de listas
assert type(separar_pares_impares(lista_prueba)) == tuple, f"Tu función debe retornar un valor de tipo {tuple.__name__}."
assert type(separar_pares_impares(lista_prueba)[0]) == list and type(separar_pares_impares(lista_prueba)[1]) == list, "La tupla que retorna tu función debe contener una lista en su primera y segunda posicion."

# Case 4: len(tupla) != 2
assert len(separar_pares_impares(lista_prueba)) == len(([],[])), "Tu función retorna una tupla de tamaño incorrecto."

# Caso 5: respuesta explicita
assert separar_pares_impares(lista_prueba) == ([2, 6, 6, 8, 8, 10], [1, 3, 7, 9]), "Tu respuesta es incorrecta para para una instancia diferente. Utiliza el parámetro."

# Caso 6: la lista de impares está ubicada antes que la lista de pares.
assert sum([i % 2 for i in separar_pares_impares(lista_prueba)[0]]) == 0, "La primera lista de la tupla debe contener únicamente pares."
assert sum([(i + 1) % 2 for i in separar_pares_impares(lista_prueba)[1]]) == 0, "La segunda lista de la tupla debe contener únicamente impares."

# Caso 7: la lista de pares y la lista de impares es cada una de longitud incorrecta
assert len(separar_pares_impares(lista_prueba)[0]) == len([2, 6, 6, 8, 8, 10]), "La primera lista de la tupla que retorna tu función no tiene la longitud correcta."
assert len(separar_pares_impares(lista_prueba)[1]) == len([1, 3, 7, 9]), "La segunda lista de la tupla que retorna tu función no tiene la longitud correcta."

# Caso 8: las listas son correctas, independiente de su orden
assert set(separar_pares_impares(lista_prueba)[0]) == {2, 6, 6, 8, 8, 10}, "La primera lista de la tupla que retorna tu función no contiene los elementos esperados, independiente de su orden."
assert set(separar_pares_impares(lista_prueba)[1]) == {1, 3, 7, 9}, "La segunda lista de la tupla que retorna tu función no contiene los elementos esperados, independiente de su orden."

# Caso 9: las listas no están ordenadas ascendentemente
assert separar_pares_impares(lista_prueba)[0] == [2, 6, 6, 8, 8, 10], "La primera lista de la tupla que retorna tu función no está ordenada ascendentemente."
assert separar_pares_impares(lista_prueba)[1] == [1, 3, 7, 9], "La segunda lista de la tupla que retorna tu función no está ordenada ascendentemente."

assert separar_pares_impares(lista)[0] == [2, 4, 6 ,8], "La primera lista de la tupla que retorna tu función no está ordenada ascendentemente."
assert separar_pares_impares(lista)[1] == [3, 5, 5, 7], "La segunda lista de la tupla que retorna tu función no está ordenada ascendentemente."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 4
# 
# A continuación, encuentras declarados algunos números enteros.

# In[ ]:


treinta = 30
cuarenta_y_cinco = 45
cincuenta = 50
sesenta_y_tres = 63


# Implementa una función anónima que reciba un número entero por parámetro (por ejemplo, la variable `trinta`) y retorne `True` si el número es mayor a 50. Guarda la función (sin ejecutar) en una variable llamada `mayor_a_cincuenta`.
# 
# *Esta función debe retornar un valor booleano* (`True` o `False`).

# In[27]:


# YOUR CODE HERE
mayor_a_cincuenta = lambda x: 1 if x>50 else 0

#raise NotImplementedError()


# In[28]:


## AUTO-CALIFICADOR

# Base variables
treinta = 30
cuarenta_y_cinco = 45
cincuenta = 50
sesenta_y_tres = 63
    
# Caso 1: no existe la función.
try:
    mayor_a_cincuenta
    assert type(mayor_a_cincuenta) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada mayor_a_cincuenta.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    mayor_a_cincuenta(treinta)
    mayor_a_cincuenta(cuarenta_y_cinco)
    mayor_a_cincuenta(cincuenta)
    mayor_a_cincuenta(sesenta_y_tres)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: la función no es de tipo lambda
assert str(mayor_a_cincuenta).find("lambda") > -1, "Tu función no es anónima o de tipo lambda."

# Caso 4: la función retorna un valor no booleano
assert type(mayor_a_cincuenta(sesenta_y_tres)) == bool, f"Tu función debe retornar un valor de tipo {bool.__name__}."

# Caso 5: condición contraria (num < 50)
assert mayor_a_cincuenta(sesenta_y_tres) and not mayor_a_cincuenta(treinta), "La condición de tu función es incorrecta. Es probable que tengas que utilizar un símbolo de desigualdad contrario."

# Caso 6: usa mayor o igual
assert not mayor_a_cincuenta(cincuenta), "50 no es mayor a 50."

# Caso 7: diversos casos
try:
    assert not mayor_a_cincuenta(treinta)
    assert not mayor_a_cincuenta(cuarenta_y_cinco)
    assert not mayor_a_cincuenta(cincuenta)
    assert mayor_a_cincuenta(sesenta_y_tres)
except AssertionError as e:
    e.args += ("Tu función no retorna el booleano correcto.",)
    raise e
    
# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 5
# 
# A continuación, encuentras declarada una lista de números enteros.

# In[ ]:


lista = [3, 4, 2, 5, 5, 6, 3]


# Implementa una función llamada `modulo_del_minimo` que reciba una lista de números enteros por parámetro (por ejemplo, la variable `lista`), encuentre el valor más pequeño que se repita en la lista (`min_val_rep`) y retorne una función anónima. Esta función anónima debe recibir un número entero mayor a cero (`entero`) por parámetro y retornar el residuo de la división entre `min_val_rep` y `entero` (recomendamos usar el operador de residuo `%`).
# 
# *Esta función debe retornar una función anónima*.
# 
# ##### Ejemplo
# ```python
#     anon = modulo_del_minimo([3, 4, 2, 5, 5, 6, 3])
#     
#     anon(2) == 1
# ```
# Una vez implementada la función `modulo_del_minimo`, ejectar el código anterior en una celda de Jupyter debe generar el *output* `True`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


## AUTO-CALIFICADOR

# Base variables:
lista = [3, 4, 2, 5, 5, 6, 3]
lista_prueba = [6, 7, 4, 5, 8, 12, 15, 15, 8]

# Caso 1: no existe la función.
try:
    modulo_del_minimo
    assert type(modulo_del_minimo) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada modulo_del_minimo.")

# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    modulo_del_minimo(lista)
    modulo_del_minimo(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")
    
# Caso 3: la función no retorna una función anónima
try:
    assert type(modulo_del_minimo(lista_prueba)) == type(lambda:None)
    assert str(modulo_del_minimo(lista_prueba)).find("lambda") > -1
except:
    raise TypeError("Tu función debe retornar una función anónima (de tipo lambda).")
    
# Caso 4: la función anónima retornada es interrumpida por errores durante su ejecución.
try:
    for i in range(100):
        modulo_del_minimo(lista)(i + 1)
        modulo_del_minimo(lista_prueba)(i + 1)
except:
    raise RuntimeError("Se produce un error al ejecutar la función anónima que retorna tu función.")
    
# Caso 5: la función anónima retornada retorna algo distinto de un entero.
assert type(modulo_del_minimo(lista_prueba)(7)) == int, f"La función anónima que retorna tu función debería retornar un valor de tipo {type(0)}."
    
# Caso 6: el sentido del cálculo del residuo es incorrecto.
try:
    assert modulo_del_minimo(lista_prueba)(0) != 0
except AssertionError as e:
    raise ArithmeticError("La función anónima que retorna tu función calcula el residuo de la división de manera incorrecta. Prueba cambiar el orden de los elementos alrededor del operador '%'",)
except ZeroDivisionError as e:
    pass
    
# Caso 7: no identifica el menor elemento que se repite correctamente.
try:
    assert modulo_del_minimo(lista)(float("inf")) == 3
    assert modulo_del_minimo(lista_prueba)(float("inf")) == 8
except AssertionError as e:
    e.args += ("La función anónima que retorna tu función utiliza un valor inesperado en lugar del mínimo valor repetido en la lista.",)
    raise e
    
# Caso 8: diversos casos
try:
    assert modulo_del_minimo(lista_prueba)(4) == 0
    assert modulo_del_minimo(lista_prueba)(5) == 3
    assert modulo_del_minimo(lista_prueba)(8) == 0
    assert modulo_del_minimo(lista_prueba)(15) == 8
    assert modulo_del_minimo(lista)(3) == 0
    assert modulo_del_minimo(lista)(5) == 3
except AssertionError as e:
    e.args += ("Tu función retorna una función anónima incorrecta.",)
    raise e
    
# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Créditos
# 
# __Autor(es)__: Camilo Falla Moreno, Alejandro Mantilla Redondo, Juan David Reyes, Diego Alejandro Cely Gómez
#  
#  __Fecha última actualización__: 06/08/2021
