from core.auth import login_flow, register_new_client
from core.menus import client_menu, employee_menu
from config.messages import (WELCOME_MESSAGE, GOODBYE_MESSAGE,INVALID_OPTION_MESSAGE)

def main():
    print(WELCOME_MESSAGE)

    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrate como nuevo cliente")
        print("3. Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            user = login_flow()
            if user is None:
                continue
            if user.role == "client":
                client_menu(user)
            elif user.role == "employee":
                employee_menu(user)
            break

        elif option == "2":
            register_new_client()
        
        elif option =="3":
            break

        else:
            print(INVALID_OPTION_MESSAGE)
    
    print(GOODBYE_MESSAGE)


if __name__ == "__main__":
    main()
