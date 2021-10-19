# Search methods

import search

# Ejemplo 1
ab = search.GPSProblem('A', 'B', search.romania)

print("\n========== Ejemplo 1 - ab ========== ")
print("\nBúsqueda con ramificación y salto: ")
resultado = search.busqueda_ramificacion_y_salto(ab)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")
print("\nBúsqueda con ramificación y salto con subestimación: ")
resultado = search.busqueda_ramificacion_y_salto_con_subestimacion(ab)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")


# Ejemplo 2
ze = search.GPSProblem('Z', 'E', search.romania)

print("\n\n========== Ejemplo 2 - ze ========== ")
print("\nBúsqueda con ramificación y salto: ")
resultado = search.busqueda_ramificacion_y_salto(ze)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")
print("\nBúsqueda con ramificación y salto con subestimación: ")
resultado = search.busqueda_ramificacion_y_salto_con_subestimacion(ze)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")


# Ejemplo 3
tg = search.GPSProblem('T', 'G', search.romania)

print("\n\n========== Ejemplo 3 - tg ========== ")
print("\nBúsqueda con ramificación y salto: ")
resultado = search.busqueda_ramificacion_y_salto(tg)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")
print("\nBúsqueda con ramificación y salto con subestimación: ")
resultado = search.busqueda_ramificacion_y_salto_con_subestimacion(tg)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")


# Ejemplo 4
cu = search.GPSProblem('C', 'U', search.romania)

print("\n\n========== Ejemplo 4 - cu ========== ")
print("\nBúsqueda con ramificación y salto: ")
resultado = search.busqueda_ramificacion_y_salto(cu)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")
print("\nBúsqueda con ramificación y salto con subestimación: ")
resultado = search.busqueda_ramificacion_y_salto_con_subestimacion(cu)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")


# Ejemplo 5
mc = search.GPSProblem('M', 'C', search.romania)

print("\n\n========== Ejemplo 5 - mc ========== ")
print("\nBúsqueda con ramificación y salto: ")
resultado = search.busqueda_ramificacion_y_salto(mc)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")
print("\nBúsqueda con ramificación y salto con subestimación: ")
resultado = search.busqueda_ramificacion_y_salto_con_subestimacion(mc)
print(f"Nodos expandidos: {resultado[1]}, Nodos visitados: {resultado[2]} \nRuta: {resultado[0].path()}")