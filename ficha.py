def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    """
    Nombre: Maria Garcia
    Email: maria.garcia@universidad.edu
    Caracteres en nombre: 12
    Iniciales: MG
    Usuario: garcia.maria
    Email valido: True
    Dominio: universidad.edu
    Nombre para archivo: Maria_Garcia
    Cantidad de a: 4
    Codigo secreto: AICRAG AIRAM
    Nota 1: 8
    Nota 2: 9
    Nota 3: 7
    Suma: 24
    Promedio: 8.0
    Promedio entero: 8
    ========================
    """
    
    nombre = input("Ingrese Nombre Completo: ")
    email = input("Ingrese Correo: ")
    nota1 = int(input("Ingrese Nota 1: "))
    nota2 = int(input("Ingrese Nota 2: "))
    nota3 = int(input("Ingrese Nota 3: "))

    nombre = nombre.strip()
    nombre = nombre.title()
    nspace = nombre.find(' ')
    email = email.lower()
    earroba = email.find('@')
    lnombre = len(nombre)
    inis = nombre[0] + nombre[nspace + 1]
    usuario = nombre[nspace + 1:].lower() + "." + nombre[0: nspace].lower()
    emailvalido = '@' in email
    dominio = email[earroba+1:]
    nombre_arch = nombre.replace(' ','_')
    count_a = nombre.count('a')
    secret_code = nombre[::-1].upper()
    sum_nots = nota1 + nota2 + nota3

    print(f"========================\n    FICHA DEL ALUMNO\n========================")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {lnombre}")
    print(f"Iniciales: {inis}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {emailvalido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_arch}")
    print(f"Cantidad de a: {count_a}")
    print(f"Codigo secreto: {secret_code}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {sum_nots}")
    print(f"Promedio: {sum_nots/3}")
    print(f"Promedio entero: {round(sum_nots/3)}")
    print("========================")

#ficha()