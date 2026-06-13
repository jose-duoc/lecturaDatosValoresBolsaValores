# Procesador de Log de Ventas de la Bolsa de Valores en Formato JSON

Este proyecto es una herramienta en Python diseñada para parsear, procesar y analizar archivos de registros (logs) de ventas. El script busca líneas específicas dentro de un archivo de texto, extrae cadenas en formato JSON embebido y genera estadísticas financieras globales y por cliente.

## 🚀 Características

* **Extracción de Datos Embebidos:** Escanea archivos de texto buscando la firma `"Data Recibida:"` para aislar el JSON.
* **Cálculo Financiero:** Suma el monto total de todas las transacciones válidas del archivo.
* **Métricas por Cliente:** Agrupa de forma automática la cantidad de compras realizadas y el gasto acumulado por cada cliente.
* **Tolerancia a Errores:** Maneja excepciones de decodificación JSON (`JSONDecodeError`) para evitar que líneas corruptas detengan la ejecución.

## 📂 Estructura del Proyecto

* `calculos.py`: Contiene la lógica de negocio, funciones de lectura de archivos, parsing de JSON y acumulación de estadísticas.
* `main.py`: Punto de entrada del programa. Coordina la ejecución y da formato a la salida en la consola.
* `datos.txt`: Archivo de entrada que contiene las líneas de log con los datos de las ventas.

## 📊 Formato de los Datos de Entrada

El script espera un archivo de texto (por defecto `datos.txt`) donde cada línea relevante contenga el prefijo `Data Recibida: ` seguido de un arreglo JSON con la información de los clientes y productos.

**Ejemplo de línea de log:**
```text
[Fecha: 2026-06-12 01:55:37] Data Recibida: [{"id_cliente":"2","cliente":"Alejandro Pérez","genero":"H","id_producto":"1","producto":"Amazon","precio":"151.48","cantidad":7,"monto":"1060.36","forma_pago":"Débito","fecreg":"2026-06-12T01:53:02.051Z"}]
