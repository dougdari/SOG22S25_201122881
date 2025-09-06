import pandas as pd
from sqlalchemy import create_engine

# ==========================
# 1. Cargar CSV limpio
# ==========================
df = pd.read_csv("ventas_tienda_online_limpio.csv")

# ==========================
# 2. Configuración conexión Railway
# ==========================
engine = create_engine(
    "mysql+pymysql://root:ppkKLvvkUxOnRngpvmcqtlBAepdviuUC@centerbeam.proxy.rlwy.net:29408/railway"
)

# ==========================
# 3. Subir datos a la tabla
# ==========================
# Si quieres reemplazar la tabla existente, usa if_exists="replace"
# Si quieres agregar los datos sin borrar, usa if_exists="append"
df.to_sql("ventas_tienda_online", con=engine, if_exists="append", index=False)

print("✅ Datos cargados exitosamente en Railway (tabla ventas_tienda_online).")
