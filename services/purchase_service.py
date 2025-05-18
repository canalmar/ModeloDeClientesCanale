from models.purchase import Purchase
from models.product import Product
from services.product_service import load_products, show_catalog
from utils.file_handler import load_json, save_json
from config.constants import PURCHASE_FILE
from config.messages import PRESS_ENTER_MESSAGE

def save_purchase (purchase: Purchase)-> None:
    """Guarda una nueva compra en el archivo JSON."""
    purchases = load_json(PURCHASE_FILE)
    purchases.append({
        "purchase_id": purchase.purchase_id,
        "user_email": purchase.user_email,
        "product_id": purchase.product_id,
        "product_title":purchase.product_title,
        "price": purchase.price,
        "date": purchase.date
    })
    save_json(purchases, PURCHASE_FILE)

def load_purchases() ->list[dict]:
    """Carga todas las compras desde el archivo JSON"""
    return load_json(PURCHASE_FILE)

def get_user_purchases(email:str) -> list[dict]:
    """Devuelve la lista de compras filtradas por email"""
    all_purchases = load_purchases() #todas las compras guardadas, cada una es un diccionario
    return [p for p in all_purchases if p.get("user_email") == email] 

def process_purchase(user_email: str):
    products = load_products()
    show_catalog(products, page_size=10)

    while True:
        selected_id = input("\nIngrese el ID del libro a comprar (o 'salir' para cancelar): ").strip()

        if not selected_id or selected_id.lower() == "salir":
            print("❌ Compra cancelada por el usuario.")
            input(PRESS_ENTER_MESSAGE)
            return

        selected_product = next((p for p in products if p.product_id == selected_id), None)
                            #next busca el primer producto en la lista con product_id igual al que ingreso el usuario
 
        if selected_product:
            break
        else:
            print("⚠️  No se encontró un libro con ese ID. Intente nuevamente.")
            continue
       
    while True:
        confirm = input(f"¿Confirmás la compra de {selected_product.title} por ${selected_product.price:.2f}? (s/n): ").lower()
        if confirm == 's':
            purchase = Purchase(user_email=user_email, product=selected_product)
            save_purchase(purchase)
            print("✅ Compra registrada exitosamente.")
            break
        elif confirm == 'n':
            print("❌ Compra cancelada.")
            break
        else:
            print("⚠️ Opción inválida. Ingresá 's' para confirmar o 'n' para cancelar.")             

    input(PRESS_ENTER_MESSAGE)

def show_purchase_summary(purchases: list[dict], include_email: bool = False):
    """Muestra una lista de compras y el total registrado.
    Si include_email=True, también muestra el email del comprador."""

    if not purchases:
        print("No hay compras registradas.")
        return

    for p in purchases:
        date = p["date"][:10]
        title = p["product_title"]
        price = p["price"]
        if include_email:
            email = p["user_email"]
            print(f"{date} - {email} - {title} - ${price:.2f}")
        else:
            print(f"{date} - {title} - ${price:.2f}")

    total = sum(p["price"] for p in purchases)
    print(f"\n💵 Total de compras registradas: ${total:.2f}")
