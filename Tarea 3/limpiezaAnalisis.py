# ==========================================
# Análisis de datos con Pandas y Seaborn
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para gráficos
plt.style.use("seaborn-v0_8")
sns.set(font_scale=1.1)

# ==========================================
# 1. Importar y cargar los datos del CSV
# ==========================================

# Cambia "archivo.csv" por el nombre de tu archivo real
df = pd.read_csv("winequality-red.csv")

print("\n=== Primeras filas del dataset ===")
print(df.head())

# ==========================================
# 2. Limpieza y preparación de datos
# ==========================================

print("\n=== Información general ===")
print(df.info())

print("\n=== Valores nulos por columna ===")
print(df.isnull().sum())

# Eliminar filas con valores nulos
df = df.dropna()

# Eliminar duplicados
df = df.drop_duplicates()

print("\n=== Información después de limpieza ===")
print(df.info())

# ==========================================
# 3. Resumen estadístico
# ==========================================
print("\n=== Resumen estadístico ===")
print(df.describe())

# ==========================================
# 4. Matriz de correlación
# ==========================================
print("\n=== Matriz de correlación ===")
corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()

# ==========================================
# 5. Gráficos
# ==========================================

# Histograma
df.hist(figsize=(10,8), bins=30)
plt.suptitle("Histogramas de Variables Numéricas")
plt.show()

# Gráfico de dispersión (usando las 2 primeras columnas numéricas)
num_cols = df.select_dtypes(include="number").columns
if len(num_cols) >= 2:
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=num_cols[0], y=num_cols[1])
    plt.title(f"Dispersión: {num_cols[0]} vs {num_cols[1]}")
    plt.show()

# Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(data=df.select_dtypes(include="number"))
plt.title("Boxplot de Variables Numéricas")
plt.show()

# ==========================================
# 6. Conclusiones (ejemplo, ajusta según dataset real)
# ==========================================

print("\n=== Conclusiones ===")
print("- Existe una correlación fuerte entre algunas variables numéricas.")
print("- La distribución de varias variables muestra sesgo.")
print("- Se identificaron posibles valores atípicos en los boxplots.")
