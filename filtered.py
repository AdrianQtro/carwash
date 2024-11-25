

def filtered_license_plate(data):
    plate = input('Digite placa a buscar: ').lower()
    filtered = list(filter(lambda x:x['Placa'].strip() == plate, data ))# lo que encontramos en esta linea. Es una nueva lista, junto a un ciclo 
    #dentro de este ciclo encontramos dos condiciones filtrandome el nombre de un lavador y la fecha 
    return filtered
    
def show_spreadsheet(data, date):
    totales = []
    total = 0
    for row in data:
        if row['Fecha'] == date:
            total += float(row['Precio'])
            totales.append(row)
    if totales:  # totales ya son preguntados en una lista en memoria
        print(f"Registros del día {date}:")
        for row in totales:
            print(f"Lavador: {row['Lavador']}, Vehículo: {row['Vehiculo']}, "
                  f"Placa: {row['Placa']}, Tipo de Lavada: {row['Tipo_lavada']}, "
                  f"Precio: {float(row['Precio']):,.0f}, Descuento: {float(row['Descuento']):,.0f}, "
                  f"Total: {float(row['Total']):,.0f}")
    else:
        print(f"No hay registros para la fecha {date}.")

    return f"Total de vehículos lavados: {len(totales)}, total de dinero que debes tener es: {total:,.0f}"


