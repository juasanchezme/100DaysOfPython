import pandas as pd

# 1. Creamos un DataFrame de ejemplo
datos = {
    'Fruta': ['Manzana', 'Banana', 'Cereza'],
    'Color': ['Roja', 'Amarillo', 'Roja']
}
df = pd.DataFrame(datos)


print("--- DataFrame Original ---")
print(df)
print("\n--- Recorriendo con iterrows() ---")

# 2. Usamos iterrows() para recorrer el DataFrame
for indice, fila in df.iterrows():
    print(f"\nÍndice de la fila: {indice}")
    
    # 'fila' es un objeto Series de pandas
    print("Contenido de la fila:")
    print(fila)
    
    # 3. Accedemos a datos específicos de la fila
    nombre_fruta = fila['Fruta']
    color_fruta = fila['Color']
    print(f"-> La fruta es {nombre_fruta} y su color es {color_fruta}.")
