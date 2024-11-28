
import car_wash_main
import expenses
from datetime import datetime

data = 'app/lavadero/carwash.csv'
data_expenses = 'app/lavadero/expenses.csv'

def total_cars(data,date):
    total_money = 0
    for row in data:
        if row['Fecha'].strip() == date:
            total_money +=  float(row['Total']) + float(row['Descuento'])      
    return total_money

def amount_expenses(data_expenses,date):
    total_exp = 0
    for row in data_expenses:
        if row['Fecha'].strip() == date:
            total_exp += float(row['Monto'])
    return total_exp

def total_income(total_money, total_exp):
    return total_money - total_exp

def calculate_total_income(date):
    # Cargar los datos
    car_wash_data = car_wash_main.read_file_csv(data)
    expenses_data = expenses.read_expenses(data_expenses)
    
    car_washing = [row for row in car_wash_data if row['Fecha'] == date]

    if car_washing:
        total_money = total_cars(car_wash_data, date)  # Total de dinero ganado
        total_exp = amount_expenses(expenses_data, date)  # Total de gastos
        total_car_wash = total_income(total_money, total_exp)  # Total neto

        return (
            f"Dinero total del día: {float(total_money):,.0f}\n"
            f"Total de gastos del día: {float(total_exp):,.0f}\n"
            f"Dinero total excluyendo gastos: {float(total_car_wash):,.0f}"
        )
    else:
        return f"La fecha {date} no existe en los registros."

def filtered_month(data,data_expenses):
    filt_income = []
    filt_exp = []
    while True:
        start_date = input('Digite fecha de inicio (dd-mm-yyyy): ').strip()
        end_date = input('Digite fecha de fin (dd-mm-yyyy): ').strip()

        if not (start_date and end_date):
            print('Para filtrar necesita llenar los campos correctamente.')
            continue

        try:
            # Convertir las fechas a objetos datetime
            start_date_obj = datetime.strptime(start_date, '%d-%m-%Y')
            end_date_obj = datetime.strptime(end_date, '%d-%m-%Y')
        except ValueError:
            print('Formato de fecha inválido. Use el formato dd-mm-yyyy.')
            continue

        for row in data:
            try:
                # Asegurarse de que `row['Fecha']` es una fecha válida
                record_date = datetime.strptime(row['Fecha'], '%d-%m-%Y')
                if start_date_obj <= record_date <= end_date_obj:
                    filt_income.append(row)
            except ValueError:
                print(f"Formato de fecha inválido en el registro: {row['Fecha']}")
                continue
        
        for row in data_expenses:
            try:
                record_date = datetime.strptime(row['Fecha'], '%d-%m-%Y')
                if start_date_obj <= record_date <= end_date_obj:
                    filt_exp.append(row)
            except ValueError:
                print(f"Formato de fecha inválido en el registro: {row['Fecha']}")
                continue
    
        if filt_income or filt_exp:
            total_income = sum(float(row['Total']) for row in filt_income) if filt_income else 0
            total_exp = sum(float(row['Monto']) for row in filt_exp) if filt_exp else 0

            total = total_income - total_exp
            print(f"Total de ingresos en el rango seleccionado: {total_income:,.0f}")
            print(f"Total de gastos en el rango seleccionado: {total_exp:,.0f}")
            print(f"Total neto (ingresos - gastos): {total:,.0f}")
            return f"Fechas filtradas: {len(filt_income)} ingresos encontrados, {len(filt_exp)} gastos encontrados."
        else:
            print("No se encontraron registros en el rango de fechas proporcionado.")
            return 'Sin registros.'