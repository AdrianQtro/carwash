import csv
import car_wash_main
from datetime import datetime

def new_record(path):
    
    while True:
        name = input('Nombre de lavador: ').strip().lower()
        vehicle = input('Vehiculo: carro/moto/camioneta: ').strip().lower()
        license_plate = input('Placa: ').strip().lower()
        type_of_washing = input('Tipo lavada: ').strip().lower()
        price = input('Precio: ')
        discount = input('Descuento: ')

        if not all([name, vehicle, license_plate, type_of_washing, price, discount]):
            print("Todos los campos son obligatorios. Por favor, completa todos los campos.")
            continue
        try:
            total = (float(price) - float(discount)) / 2
            current_date = datetime.today().date().strftime('%d-%m-%Y') # Fecha actual
        except ValueError:
            print("El precio y el descuento deben ser valores numéricos. Inténtalo de nuevo.")
            continue
        try:
            with open(path, mode='a', newline='') as file:
                fields = ['Fecha', 'Lavador', 'Vehiculo', 'Placa', 'Tipo_lavada', 'Precio', 'Descuento', 'Total']
                writer = csv.DictWriter(file, fieldnames=fields)
                
                # Write header only if the file is empty
                file.seek(0, 2)
                if file.tell() == 0:
                    writer.writeheader()
                
                # Write the new record to the CSV file
                writer.writerow({
                    'Fecha': current_date,
                    'Lavador': name,
                    'Vehiculo': vehicle,
                    'Placa': license_plate,
                    'Tipo_lavada': type_of_washing,
                    'Precio': price,
                    'Descuento': discount,
                    'Total': total
                })            
            return f'El registro a sido agregado exitosamente.'
        except  Exception as e:
            return f'Error al guardar los datos: {e}'

# Código principal
if __name__ == '__main__':
    result = new_record('app/lavadero/carwash.csv')
    data = car_wash_main.read_file_csv('app/lavadero/carwash.csv')
    print(result)