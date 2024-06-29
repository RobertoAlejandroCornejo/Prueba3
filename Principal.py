from funciones import agregar_producto, listar_productos, buscar_producto_categoria, promedio_precio, guardar_productos

# Función principal del programa
def main():
    productos = {}

    while True:
        print("\nMenú:")
        print("1. Registrar productos")
        print("2. Listar todos los productos")
        print("3. Buscar productos por categoría")
        print("4. Calcular el precio promedio de los productos")
        print("5. Salir del programa y guardar")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                agregar_producto(productos)
            elif opcion == 2:
                listar_productos(productos)
            elif opcion == 3:
                buscar_producto_categoria(productos)
            elif opcion == 4:
                promedio = promedio_precio(productos)
                print(f"El promedio de los precios ingresados es: {promedio}")
            elif opcion == 5:
                guardar_productos(productos)
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")
            
if __name__ == "__main__":
    main()

