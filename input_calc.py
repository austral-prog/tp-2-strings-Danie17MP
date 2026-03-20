def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    Base: 8
    Altura: 5
    Area: 40
    Perimetro: 26
    """
    bass = int(input("Base: "))
    heigh = int(input("Altura: "))

    print(f"Base: {bass}")
    print(f"Altura: {heigh}")
    print(f"Area: {bass * heigh}")
    print(f"Perimetro: {(bass + heigh) * 2}")

#rectangle()