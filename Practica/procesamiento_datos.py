import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("ventas_tienda_online.csv")

# ==========================
# 1. Eliminar duplicados
# ==========================
df = df.drop_duplicates()

# ==========================
# 2. Eliminar valores faltantes
# ==========================
df = df.dropna()

# ==========================
# 3. Corrección de tipos de datos
# ==========================
# Definimos los tipos esperados
tipos = {
    "order_id": "Int64",   # Int64 de pandas permite manejar nulos temporalmente
    "purchase_date": "string",
    "customer_id": "Int64",
    "customer_gender": "string",
    "customer_age": "Int64",
    "product_category": "string",
    "product_name": "string",
    "product_price": "float64",
    "quantity": "Int64",
    "order_total": "float64",
    "payment_method": "string",
    "shipping_region": "string"
}

# Convertir columnas a los tipos deseados
for col, dtype in tipos.items():
    try:
        if col == "purchase_date":
            # Convertir a formato fecha (día/mes/año)
            df[col] = pd.to_datetime(df[col], format="%d/%m/%y", errors="coerce")
        else:
            df[col] = df[col].astype(dtype)
    except Exception as e:
        print(f"⚠️ Error al convertir columna {col}: {e}")

# ==========================
# 4. Eliminar filas inválidas tras la conversión
# ==========================
df = df.dropna()

# ==========================
# 5. Guardar el archivo limpio
# ==========================
df.to_csv("ventas_tienda_online_limpio.csv", index=False)

print("Archivo limpio generado: ventas_tienda_online_limpio.csv")
