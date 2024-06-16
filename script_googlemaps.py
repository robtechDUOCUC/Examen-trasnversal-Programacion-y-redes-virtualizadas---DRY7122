import geopy.distance
import googlemaps


# Configura tu clave de API de Google Maps
API_KEY = 'AIzaSyAvsMgsIAsUYwt8_CSTFlpppSonim_LyBk'


gmaps = googlemaps.Client(key=API_KEY)


def obtener_coordenadas(ciudad):
    geocode_result = gmaps.geocode(ciudad)
    if not geocode_result:
        return None
    location = geocode_result[0]['geometry']['location']
    return (location['lat'], location['lng'])


def calcular_distancia(coord_origen, coord_destino):
    return geopy.distance.distance(coord_origen, coord_destino).km


def obtener_duracion_y_direcciones(origen, destino, modo):
    directions_result = gmaps.directions(origen, destino, mode=modo)
    if not directions_result:
        return None, None
    duration = directions_result[0]['legs'][0]['duration']['text']
    steps = directions_result[0]['legs'][0]['steps']
    narrativa = "Instrucciones del viaje:\n"
    for step in steps:
        narrativa += step['html_instructions'] + "\n"
    return duration, narrativa


def main():
    while True:
        print("Ingrese 's' para salir en cualquier momento.")
        ciudad_origen = input("Ciudad de Origen: ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break
        coord_origen = obtener_coordenadas(ciudad_origen)
        coord_destino = obtener_coordenadas(ciudad_destino)
        if not coord_origen or not coord_destino:
            print("No se pudieron obtener las coordenadas de una o ambas ciudades.")
            continue


        distancia_km = calcular_distancia(coord_origen, coord_destino)
        distancia_millas = distancia_km * 0.621371


        print("Elija el medio de transporte:")
        print("1. Auto")
        print("2. Bicicleta")
        print("3. Caminando")
        medio_transporte = input("Opción: ")


        if medio_transporte == '1':
            modo = "driving"
        elif medio_transporte == '2':
            modo = "bicycling"
        elif medio_transporte == '3':
            modo = "walking"
        else:
            print("Opción no válida. Intente de nuevo.")
            continue


        duracion, narrativa = obtener_duracion_y_direcciones(ciudad_origen, ciudad_destino, modo)


        if duracion and narrativa:
            print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
            print(f"Duración del viaje: {duracion}")
            print(narrativa)
        else:
            print("No se pudo obtener la duración o narrativa del viaje.")


if _name_ == "_main_":
    main()