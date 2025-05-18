import pandas as pd
from models.product import Product
from config.constants import PRODUCT_FILE

def load_products() -> list[Product]:
    """Carga los productos desde un archivo csv y
    devuelve una lista de objetos Product"""

    try:
        df = pd.read_csv(PRODUCT_FILE)
        products = []
        for _, row in df.iterrows():
            product = Product(
                product_id=row["ID"],
                title=row["Título"],
                author=row["Autor"],
                genre=row["Género"],
                price=float(row["Precio"])
            )
            products.append(product)
        return products
    except FileNotFoundError:
        print("⚠️ Archivo de producto no encontrado.")
        return []
    except Exception as e:
        print(f"❌  Error al cargar productos: {e}")
        return []
    
def show_catalog(products: list[Product], page_size=10) -> None:
    """Muestra el catalogo de productos"""
    print("\n📚 Catálogo de libros disponibles en Tienda de Historias:")
    total = len(products)
    for i in range(0,total,page_size):
        print(f"*** Mostrando libros {i+1} a {min(i+page_size, total)} de {total}: ***\n")
        for product in products[i:i+page_size]:
            print(product)
        if i + page_size <total:
            input("➡️  Presiona Enter para ver más...")
        else:
            print("\n 🔚  Fin del catálogo  ")