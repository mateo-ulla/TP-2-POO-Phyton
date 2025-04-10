class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_datos(self):
        herramientas = []
        for i in range(3):
            nombre = input("Nombre de la herramienta: ")
            marca = input("Marca de la herramienta: ")
            precio = int(input("Precio de la herramienta: "))
            cantidad = int(input("Cantidad de la herramienta: "))
            herramienta = {
                "nombre": nombre,
                "marca": marca,
                "precio": precio,
                "cantidad": cantidad
            }
            herramientas.append(herramienta)
        
        print("\n=== Lista de herramientas ingresadas ===")
        for i, h in enumerate(herramientas, start=1):
            print(f'''Herramienta #{i}:
  NOMBRE: {h["nombre"]}
  MARCA: {h["marca"]}
  PRECIO: {h["precio"]}
  CANTIDAD: {h["cantidad"]}\n''')

Herramientas = Nodo("Herramientas")
Herramientas.mostrar_datos()
