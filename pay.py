
def totalcars(data):
    total = 0
    totales = []
    name = input('Digite nombre de lavador a pagar: ').strip().lower()  
    lavadores = [row['Lavador'] for row in data]  # recorremos la columna de row['Lavador] y le preguntamos si es igual a name 
    if name in lavadores: 
        date = input('Digite fecha(formato DD-MM-YYYY): ')
        for row in data:
            if  row['Fecha'] == date.strip():
                totales.append(row)
                total += float(row['Total'])
        if totales:  # totales ya son preguntados en una lista en memoria
            for row in totales:
                print(f"Lavador: {row['Lavador']}, Vehículo: {row['Vehiculo']}, "
                    f"Placa: {row['Placa']}, Tipo de Lavada: {row['Tipo_lavada']}, "
                    f"Precio: {float(row['Precio']):,.0f}, Descuento: {float(row['Descuento']):,.0f}, "
                    f"Total: {float(row['Total']):,.0f}")  
                
            return f'Total de carros lavados: {len(totales)}, Total a pagar: {total:,.0f}'
        else: 
            return F'No se encontraron registros para el lavador: {name}'# se ejecuta cuando ingresaste un nombre, pero la fecha no coincide.(no existe)
    else:
        return f'El nombre {name} no existe en los registros.'
    

# ESTA FUNCION TIENE DOS VALIDACIONES, PRIMERO, PREGUNTA EL NOMBRE Y VALIDA SI EXISTE EN DATA.
# SI EL NOMBRE EXISTE EN LOS RGISTRO, PASA AL FILTRO DE FECHA. Y SI NO COINCIDE, SE EJECUTA ESTE ELSE: 
           # else:
           # return F'No se encontraron registros para el lavador: {name}'
# SI EL NOMBRE Y LA FECHA COINCIDEN CON EL MISMO DIA, QUIERE DECIR SI EXISTE E IMPRIME LOS REGISTROS EN TOTALES.
