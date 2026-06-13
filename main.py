from calculos import leer_y_calcular_total,obtener_estadisticas_clientes
def main():
    archivo_txt = "datos.txt"
    print("Procesando el archivo de ventas...")
    total = leer_y_calcular_total(archivo_txt)
    print("-"*40)
    print(f"El monto total de todas las ventas es: ${total:,.2f}")
    print("-"*40)

    print("=== ESTADÍSTICAS POR CLIENTE ===")
    clientes_datos = obtener_estadisticas_clientes(archivo_txt)
    for cliente,datos in clientes_datos.items():
        print(f"Cliente: {cliente}")
        print(f" - Cantidad de compras: {datos['compras']}")
        print(f" - Total gastado: ${datos['total_gasto']:,.2f}")
        print("-" * 30)
if __name__ == "__main__":
    main()