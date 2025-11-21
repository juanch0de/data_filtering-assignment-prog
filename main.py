import api2
import ui

def main():

    # Entradas del usuario
    departamento, municipio, cultivo, n = ui.get_user_input()

    # Cargar datos
    headers, data = api2.load_data("corregido4.xlsx")

    # Filtrar
    filtered = api2.filter_data(headers, data, departamento, municipio, cultivo, n)

    if not filtered:
        print("\nNo se encontraron registros con esos criterios.")
        return

    # Calcular medianas
    medians = api2.calculate_medians(headers, filtered)

    # Construir tabla
    table, medians = api2.build_output_table(headers, filtered, medians)

    # Mostrar al usuario
    ui.display_results(table, medians)


if __name__ == "__main__":
    main()

