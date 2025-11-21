def get_user_input():
    departamento = input("Ingrese el Departamento: ")
    municipio = input("Ingrese el Municipio: ")
    cultivo = input("Ingrese el Cultivo: ")
    n = int(input("Número de registros a consultar: "))
    return departamento, municipio, cultivo, n


def display_results(table, medians):

    print("\n=== RESULTADOS ===")
    print("\nRegistros encontrados:\n")

    headers = ["Departamento", "Municipio", "Cultivo", "Topología"]
    print("{:15} {:15} {:15} {:15}".format(*headers))

    for row in table:
        print("{:15} {:15} {:15} {:15}".format(*[str(x) for x in row]))

    print("\nMedianas:")
    print(f"pH: {medians['mediana_ph']}")
    print(f"Fósforo (P): {medians['mediana_p']}")
    print(f"Potasio (K): {medians['mediana_k']}")

