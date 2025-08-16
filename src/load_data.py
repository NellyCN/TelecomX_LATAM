import pandas as pd

def cargar_datos():
    ruta = "data/TelecomX_Data.json"
    try:
        df = pd.read_json(ruta)
        print("✅ Datos cargados correctamente.")
        print("\n📊 Primeras filas:")
        print(df.head())

        print("\n📌 Info del DataFrame:")
        df.info()

        print("\n🧪 Tipos de datos:")
        print(df.dtypes)
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")

if __name__ == "__main__":
    cargar_datos()
