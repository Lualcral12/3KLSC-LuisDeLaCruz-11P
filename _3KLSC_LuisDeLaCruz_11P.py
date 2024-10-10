def generarTablas():
    tabla = 1
    cantidad_tablas = int(input("¿Cuántas tablas deseas generar? "))

    while tabla <= cantidad_tablas:
        multiplicador = 10
        while multiplicador >= 1:
            print(f"{tabla} x {multiplicador} = {tabla * multiplicador}")
            multiplicador -= 1
        input("Presiona Enter para continuar...")
        tabla += 1


def tablaEspecifica():
    multiplicador = 1
    numero = int(input("Ingresa el número para generar su tabla: "))

    while multiplicador <= 12:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador += 1

    input("Presiona Enter para continuar...")

generarTablas()
tablaEspecifica()
