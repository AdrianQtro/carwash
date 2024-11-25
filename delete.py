import csv

def delete_record(path,data):
    date = input('Para eliminar registro digite fecha(formato DD-MM-YYYY): ').strip()
    plate = input('Digite placa: ').strip()
    registro_encontrado = None
    for row in data:
        if row['Fecha'] == date and row['Placa'] == plate:
            registro_encontrado = row
            break
    if registro_encontrado:
        print(f"Registro encontrado: Fecha: {registro_encontrado['Fecha']}, Placa: {registro_encontrado['Placa']}, "
                f"Vehículo: {registro_encontrado['Vehiculo']}, Tipo de lavada: {registro_encontrado['Tipo_lavada']}, Precio: {registro_encontrado['Precio']}")
        confirmar = input('Estas seguro de eliminar este registro ? ')
        if confirmar == 'si':
             # Se Filtra la lista excluyendo el registro encontrado
            data = [row for row in data if row != registro_encontrado]  
            with open(path, mode = 'w', newline ='' ) as file:
                fields = ['Fecha', 'Lavador', 'Vehiculo', 'Placa', 'Tipo_lavada', 'Precio', 'Descuento', 'Total']
                writer = csv.DictWriter(file, fieldnames = fields) # sobreescribiendo el archivo, ya sin el dato que no paso el filtro
                writer.writeheader()
                writer.writerows(data)

            print("El registro se eliminó correctamente.")
            return True # el boolean con el confirmar 
        else:
            print("Eliminación cancelada por el usuario.")
            return False
    else:
        return f"No se encontró ningún registro con Fecha: {date} y Placa: {plate}."
