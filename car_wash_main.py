import csv
import add_wash
import filtered
import pay 
import delete
import total_day
from datetime import datetime
from expenses import secundary_menu

path = "/home/adrian/lavadero/carwash.csv"
ARCHIVO = '/home/adrian/lavadero/expenses.csv'

def read_file_csv(path):
    try:
        data = []
        with open(path, 'r')as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"El archivo no se encuentra en la ruta: {path}")

def main_menu():
    data = read_file_csv('/home/adrian/lavadero/carwash.csv')
    data_expenses = read_file_csv('/home/adrian/lavadero/expenses.csv')
    while True:
        print("************************")
        print("*** MENU DE OPCIONES ***")
        print("************************")
        print("1. Agregar lavada")
        print("2. Mostrar planilla")
        print("3. Pagar")
        print("4. Eliminar Registro en planilla")
        print("5. Departamento de Gastos")
        print("6. Total del dia")
        print("7. Total del mes")
        print("8. Buscar por placa")
        print("9. Salir")
        
        opcion = input("Seleccione una de las siguientes opciones: ")

        if opcion == "1":
            result_add = add_wash.new_record(path)
            print(result_add)

        elif opcion == "2":
            today = datetime.now().strftime('%d-%m-%Y')
            result_sheet = filtered.show_spreadsheet(data, today)
            print(result_sheet)

        elif opcion == "3":
            result_pay = pay.totalcars(data)
            print(result_pay)
            
        elif opcion == "4":
            result_delete = delete.delete_record(path,data)
            print(result_delete)
            
        elif opcion == "5":
            secundary_menu(data_expenses)
            
        elif opcion == "6":
            date = input("Digite la fecha (formato DD-MM-YYYY): ").strip()
            result = total_day.calculate_total_income(date)  
            print(result)

        elif opcion == "7":
            result_month = total_day.filtered_month(data,data_expenses)
            print(result_month)

        elif opcion == "8":
            result_plate = filtered.filtered_license_plate(data)
            print(result_plate)
        
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == '__main__':
    data = read_file_csv("/home/adrian/lavadero/carwash.csv")
    main_menu()    
    

   

    

    
   


    
    
