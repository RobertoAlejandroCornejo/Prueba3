import random
import math

def agregar_producto(productos):
    precio = random.randint(1, 1000)
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")

    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }

    producto[nombre] = producto
    print(f"Producto ingresado correctamente con precio {precio}")

def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Lista de productos registradas:")
        for precio, producto in productos.items():
            print(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, cantidad: {producto['cantidad']}, precio: {producto['precio']}")
            print()

def buscar_producto_categoria(productos):
    categoria = input("Ingrese la categoría para buscar productos: ")
    encontrados = False

    for cod, producto in productos.items():
        if producto["categoria"].lower() == categoria.lower():
            if not encontrados:
                print(f"Productos encontrados en la categoría '{categoria}':")
                encontrados = True
            
            print(f" Nombre: {producto['nombre']}, Categoria: {producto['categoria']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
    
    if not encontrados:
        print(f"No se encontraron productos en la categoría '{categoria}'.")


def promedio_precio(productos):
    precio = [int(producto["precio"]) for producto in productos.values()]
    promedio_precio = math.promedio(precio)
    return promedio_precio

def guardar_productos(productos):
    archivo = "Productos.txt"
    with open(archivo, 'w') as f:
        for producto in productos.values():
            f.write(f"Nombre: {producto['nombre']}\n")
            f.write(f"Categoria: {producto['categoria']}\n")
            f.write(f"Cantidad: {', '.join(producto['cantidad'])}\n")
            f.write(f"Precio: {producto['precio']}\n")
            f.write("\n")

    print(f"Productos guardadas correctamente en el archivo '{archivo}'.")
