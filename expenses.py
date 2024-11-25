
import csv
from datetime import datetime
ARCHIVO = 'app/lavadero/expenses.csv'


def read_expenses(ARCHIVO):
    data_expenses = []
    with open(ARCHIVO,mode='r')as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_expenses.append(row)
        return data_expenses
    
def secundary_menu():
    while True:
        print("************************")
        print("*** MENU DE OPCIONES ***")
        print("************************")
        print("1. Agregar Gasto")
        print("2. Ver gastos del dia")
        print("3. Eliminar gasto")
        print("4. Salir")
        
        opcion = input("Seleccione una de las siguientes opciones: ")
        
        if opcion == "1":
            result_add = add_exp(ARCHIVO)
            print(result_add)

        elif opcion == "2":
            result_exp = total_exp(data_expenses)# gastos del dia 
            print(result_exp)# NOTA: LOS VALORES RETORNADOS NESECITAN SER EJECUTADOS MEDIANTE UNA VARIABLE PARA LUEGO SER IMPRESOS 

        elif opcion == "3":
            result_delete = delete_exp(data_expenses,ARCHIVO)
            print(result_delete)
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


def add_exp(ARCHIVO):
    while True:
        current_date = datetime.today().date().strftime('%d-%m-%Y')
        description = input('Descripcion: ').strip().lower()
        if not description:
            print('Por favor complete la descripcion, sea breve')
            continue
        try:
            amount = int(input('Digite el monto: '))
            if amount <= 0:
                print(f'El monto debe ser un numero positivo.')
                continue
        except ValueError: # error por dato numerico
            print(f'El monto debe ser un dato numerico.')
            continue

        try:
            with open(ARCHIVO, mode='a', newline='') as file:
                fields = ['Fecha', 'Descripcion_Gasto', 'Monto']
                writer = csv.DictWriter(file, fieldnames=fields)

                file.seek(0, 2)
                if file.tell() == 0:
                    writer.writeheader()
                
                writer.writerow({
                        'Fecha': current_date,
                        'Descripcion_Gasto': description,
                        'Monto': amount                    
                    })  
            print(F'{amount:,.0f} agregado correctamente a los gastos del dia. {current_date}')
            return f'Gasto registrado: {amount:,.0f} el {current_date} con descripción "{description}"'
            #VEO QUE CON EL RETURN NO NESECITARIA EL BREAK DEL WHILE TRUE 
        except Exception as e:
            return f'Error al guardar los datos: {e}'
            
    
def total_exp(data_expenses):
    daily_expenses = []
    totals = 0
    date = input('Digite fecha(formato DD-MM-YYYY): ').strip()
    for row in data_expenses:
        if row['Fecha'].strip() == date:
            totals += float(row['Monto'])
            daily_expenses.append(row)
    if daily_expenses: # Si existen gastos diarios, entonces imprimalos en el siguiente ciclo
        print(f"Gastos del día {date}:")
        for expense in daily_expenses:
            print(f"Gasto: {expense['Descripcion_Gasto']}, "
                f"Monto: {float(expense['Monto']):,.0f}")
        return f"Suma total de gastos: {totals:,.0f} "
    else:
        return f'No se encontro ningun gasto en este dia.'

def delete_exp(data_expenses,ARCHIVO):
    date = input('Digite fecha del gasto a eliminar (formato DD-MM-YYYY): ')
    description = input('Digite descripcion exacta del gasto: ')
    registro_encontrado = None
    for row in data_expenses:
        if row['Fecha'] == date and row['Descripcion_Gasto'] == description:
            registro_encontrado = row
            break
    if registro_encontrado:
        print(f"Registro encontrado: Fecha: {registro_encontrado['Fecha']}, "
              f"Descripcion del gasto: {registro_encontrado['Descripcion_Gasto']}, Monto: {registro_encontrado['Monto']}")
        confirmar = input('Estas seguro de eliminar este gasto ? ')
        if confirmar == 'si':
            data_expenses = [row for row in data_expenses if row != registro_encontrado]
            with open(ARCHIVO, mode = 'w', newline ='' ) as file:
                    fields = ['Fecha', 'Descripcion_Gasto', 'Monto']
                    writer = csv.DictWriter(file, fieldnames = fields) # sobreescribiendo el archivo, ya sin el dato que no paso el filtro
                    writer.writeheader()
                    writer.writerows(data_expenses)
            return f'El gasto se elimino correctamente.'
        else: # NOTA AQUI NO ESTOY CON UN WHILE TRUE, QUE ES DONDE DEBO DE COLOCAR UN PRINT( ) Y RETURN
            return f'La eliminacion del gasto No pudo completarse.'
    else:
        return f'No se encontro ningun registro con los datos ingresados.'

if __name__ == '__main__':
    data_expenses = read_expenses('app/lavadero/expenses.csv')
    secundary_menu()
    
    
    




