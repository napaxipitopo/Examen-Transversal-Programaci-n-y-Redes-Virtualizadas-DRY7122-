# Script básico para calcular viajes entre ciudades de Chile y Argentina

# Distancias en km (aproximadas)
distancias_km = {
    ("Santiago", "Buenos Aires"): 1400,
    ("Valparaíso", "Mendoza"): 950,
    ("Concepción", "Rosario"): 1100,
    ("Antofagasta", "Salta"): 1800,
    ("La Serena", "Córdoba"): 1350,
    ("Antofagasta", "Buenos Aires"): 1800,
    ("Santiago", "Córdoba"): 1100,
    ("Santiago", "Mendoza"): 1050
}

# Velocidades promedio (km/h)
velocidades = {
    "auto": 80,
    "autobús": 60,
    "avión": 800
}

# Ciudades disponibles según transporte
ciudades_origen = list(set([ori for ori, des in distancias_km]))
ciudades_destino = list(set([des for ori, des in distancias_km]))

# Ciudades con vuelos
origen_avion = ["Santiago", "Antofagasta"]
destino_avion = ["Mendoza", "Buenos Aires", "Córdoba"]

def km_a_millas(km):
    return km * 0.621371

def mostrar_opciones(lista):
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")

def elegir_opcion(lista, texto):
    while True:
        try:
            opcion = int(input(texto))
            if 1 <= opcion <= len(lista):
                return lista[opcion - 1]
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except:
            print("Entrada no válida. Ingrese el número de la opción.")

def convertir_a_horas_y_minutos(decimal_horas):
    horas = int(decimal_horas)
    minutos = int(round((decimal_horas - horas) * 60))
    return horas, minutos

print("=== Calculadora de Viajes Chile - Argentina ===\n")

while True:
    # Elegir medio de transporte
    print("Seleccione medio de transporte:")
    medios = ["auto", "autobús", "avión"]
    mostrar_opciones(medios)
    print("S. Salir")

    op_transporte = input("Ingrese una opción: ").lower()
    if op_transporte == 's':
        break
    elif op_transporte in ['1', '2', '3']:
        transporte = medios[int(op_transporte) - 1]
    else:
        print("Opción inválida. Intente nuevamente.\n")
        continue

    # Mostrar opciones de ciudad de origen
    if transporte == "avión":
        print("\nCiudades disponibles para viajar en avión (origen):")
        mostrar_opciones(origen_avion)
        origen = elegir_opcion(origen_avion, "Seleccione ciudad de origen: ")
    else:
        print("\nCiudades disponibles como origen:")
        mostrar_opciones(ciudades_origen)
        origen = elegir_opcion(ciudades_origen, "Seleccione ciudad de origen: ")

    # Mostrar opciones de ciudad de destino
    if transporte == "avión":
        print("\nCiudades disponibles para llegar en avión (destino):")
        mostrar_opciones(destino_avion)
        destino = elegir_opcion(destino_avion, "Seleccione ciudad de destino: ")
    else:
        print("\nCiudades disponibles como destino:")
        mostrar_opciones(ciudades_destino)
        destino = elegir_opcion(ciudades_destino, "Seleccione ciudad de destino: ")

    # Validar ruta
    if (origen, destino) in distancias_km:
        distancia_km = distancias_km[(origen, destino)]
    elif (destino, origen) in distancias_km:
        distancia_km = distancias_km[(destino, origen)]
    else:
        print(f"\nNo existe una ruta registrada entre {origen} y {destino}.\n")
        continue

    # Elegir unidad de distancia
    unidad = input("\n¿Desea ver la distancia en kilómetros o millas? (k/m): ").lower()
    if unidad not in ['k', 'm']:
        print("Unidad inválida. Mostraremos en kilómetros por defecto.\n")
        unidad = 'k'

    # Cálculo de duración
    velocidad = velocidades[transporte]
    duracion = distancia_km / velocidad
    horas, minutos = convertir_a_horas_y_minutos(duracion)

    # Mostrar resultados
    print("\n--- Detalles del viaje ---")
    print("Medio de transporte:", transporte)
    print("Origen:", origen)
    print("Destino:", destino)
    if unidad == 'm':
        print("Distancia:", round(km_a_millas(distancia_km), 2), "millas")
    else:
        print("Distancia:", distancia_km, "km")
    print(f"Duración estimada: {horas} hora(s) y {minutos} minuto(s)")
    print(f"Viajar desde {origen} a {destino} en {transporte} tomará aproximadamente {horas}h {minutos}min.\n")

print("¡Gracias por usar la calculadora de viajes!")

