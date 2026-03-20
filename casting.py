def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total.
    Precio: 150
    Descuento: 23.5
    Precio con descuento: 126.5
    Total: 379.5
    """
    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input("Cantidad: "))

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    new_price = precio - descuento

    print(f"Precio con descuento: {new_price}")
    print(f"Total: {new_price * cantidad}")

#casting()