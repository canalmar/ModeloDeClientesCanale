from core.auth import register_new_client
from services.product_service import load_products, show_catalog
from services.purchase_service import get_user_purchases, load_purchases, process_purchase, show_purchase_summary
from services.user_service import load_users,find_user_by_email
from utils.validators import is_valid_email
from config.messages import ( INVALID_OPTION_MESSAGE, PRESS_ENTER_MESSAGE, INVALID_EMAIL_FORMAT_MESSAGE)

def client_menu(user):
    while True:      
        print(f"\n 📚 ¡Hola {user.first_name}! 📚\nAbrí las puertas de Tienda de Historias...✨\n")
        print("1. Explorar nuestro catálogo de libros")
        print("2. Comprar el libro que te gusta")
        print("3. Ver tu historial de compras")
        print("4. Cerrar sesión")

        option = input("\nSelecciona una opción: ").strip()

        if option == "1":
            products = load_products()
            show_catalog(products)
            input(PRESS_ENTER_MESSAGE)

        elif option == "2":
            process_purchase(user.email)

        elif option == "3":
            print("\n🧾 Mi historial de compras en Tienda de Historias:")
            purchases = get_user_purchases(user.email)

            if not purchases:
                print("Aún no realizaste compras.")
                input(PRESS_ENTER_MESSAGE)
            else:
                show_purchase_summary(purchases)
                input(PRESS_ENTER_MESSAGE)

        elif option == "4":
            print("\nCerrando sesión...")  
            break
        else:
            print(INVALID_OPTION_MESSAGE)

def employee_menu(user):
    while True:
        print(f"\n📖 Menú de Gestión de Tienda de Historias\n")
        print("1. Ver catálogo")
        print("2. Ver clientes registrados")
        print("3. Registrar nuevo cliente")
        print("4. Registrar una nueva compra")
        print("5. Ver historial de compra de un cliente")
        print("6. Ver historial de compra de todos los clientes")
        print("7. Cerrar sesión")

        option = input("\nSelecciona una opción: ").strip()

        if option == "1":
            products = load_products()
            show_catalog(products,page_size=10)
            input(PRESS_ENTER_MESSAGE)

        elif option == "2":
            print("\n👥 Clientes registrados:")
            
            users = load_users()
            clients = [u for u in users if u.role == "client"]
            if not clients:
                print("No hay clientes registrados.")
            else:
                for c in clients:
                    print(c)
                input(PRESS_ENTER_MESSAGE)    

        elif option == "3":
            register_new_client()
            
        elif option == "4":
            print("\n🛒 Registrar una compra para un cliente")
            email = input("Ingrese el email del cliente: ").strip()

            if not is_valid_email(email):
                print(INVALID_EMAIL_FORMAT_MESSAGE)
                input(PRESS_ENTER_MESSAGE)
                continue

            users = load_users()
            client = find_user_by_email(email, users)

            if not client or client.role != "client":
                print("⚠️ No se encontró un cliente con ese email.")
                input(PRESS_ENTER_MESSAGE)
                continue
        
            process_purchase(email)

        elif option == "5":
            print("\n📧 Buscar historial de un cliente por email:\n")

            email = input("Ingrese el email del cliente: ").strip()

            if not is_valid_email(email):
                print(INVALID_EMAIL_FORMAT_MESSAGE)
                input(PRESS_ENTER_MESSAGE)
                continue

            purchases = get_user_purchases(email)

            if not purchases:
                print("No hay compras registradas.")
            else:
                show_purchase_summary(purchases)
                   
            input(PRESS_ENTER_MESSAGE)        

        elif option == "6":
            print("\n📖 Historial de compras de todos los clientes:\n")

            purchases = load_purchases() # lista de compras desde JSON

            if not purchases:
                print("No hay compras registradas.")
            else:
                show_purchase_summary(purchases, include_email=True)

            input(PRESS_ENTER_MESSAGE)        

        elif option == "7":
            print("\n Cerrando sesión de empleado...")
            break

        else:
            print(INVALID_OPTION_MESSAGE)

