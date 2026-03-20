def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    name1 = input("Nombre: ")
    last_name = input("Apellido: ")
    complet_name = name1 + " " + last_name


    print(complet_name.lower())
    print(complet_name.title())
    print(complet_name.upper())
    print(f"\t{complet_name.lower()}")

#names()