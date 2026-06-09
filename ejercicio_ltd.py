'''
Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2026-01-01»).
«producto»: una cadena de texto que represente el nombre del producto vendido.
«cantidad»: un número entero que represente la cantidad de productos vendidos.
«precio»: un número flotante que represente el precio unitario del producto.


'''

ventas = [
    {"fecha": "2026-01-01", "producto": "lapices", "cantidad": 100, "precio": 22.5},
    {"fecha": "2026-01-02", "producto": "block de notas", "cantidad": 50, "precio": 35.0},
    {"fecha": "2026-01-03", "producto": "cuadernos", "cantidad": 80, "precio": 52.0},       
    {"fecha": "2026-01-04", "producto": "temperas", "cantidad": 30, "precio": 40.0},
    {"fecha": "2026-01-05", "producto": "goma de borrar", "cantidad": 120, "precio": 20.0},      
    {"fecha": "2026-01-06", "producto": "reglas", "cantidad": 30, "precio": 16.0},  
    {"fecha": "2026-01-08", "producto": "plumones", "cantidad": 10, "precio": 30.0}

]
'''
#iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]     
print("Los ingresos totales generados por todas las ventas son:", ingresos_totales)

# el resultado de la suma de los ingresos totales generados por todas las ventas es: 12250.0


#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = {}
for articulo in ventas:
    producto = articulo["producto"]
    cantidad = articulo["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

articulo_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("El producto más vendido es:", articulo_mas_vendido)
'''
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

precios_por_producto = {}
for articulo in ventas:
    producto = articulo["producto"]
    precio = articulo["precio"]
    cantidad = articulo["cantidad"]
    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + (precio * cantidad), total_unidades + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    precio_promedio = suma_precios / total_unidades if total_unidades > 0 else 0
    print(f"El precio promedio de {producto} es: {precio_promedio}")


#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
'''
ingresos_por_dia = {}
for articulo in ventas:
    fecha = articulo["fecha"]
    ingreso = articulo["cantidad"] * articulo["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

for fecha, ingresos in ingresos_por_dia.items():
    print(f"Los ingresos del {fecha} son: {ingresos}")



Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
«cantidad_total»: la cantidad total vendida del producto.
«ingresos_totales»: los ingresos totales generados por la venta del producto.
«precio_promedio»: el precio promedio de venta del producto.
'''



resumen_ventas = {}
for articulo in ventas:
    producto = articulo["producto"]
    cantidad = articulo["cantidad"]
    precio = articulo["precio"]
    ingreso = cantidad * precio
    
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += ingreso
    else:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad,
            "ingresos_totales": ingreso,
            "precio_promedio": 0
        }       
for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"] if datos["cantidad_total"] > 0 else 0        
for producto, datos in resumen_ventas.items():
    print(f"Producto: {producto}")
    print(f"Cantidad Total Vendida: {datos['cantidad_total']}")
    print(f"Ingresos Totales: {datos['ingresos_totales']}")
    print(f"Precio Promedio: {datos['precio_promedio']}\n")

