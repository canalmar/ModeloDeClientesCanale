import re
from models.user import Client, Employee
from services.user_service import create_user, load_users, save_users, find_user_by_email, is_email_registered
from utils.validators import is_valid_email
from config.messages import (LOGIN_CANCEL_MESSAGE, INVALID_EMAIL_FORMAT_MESSAGE,
    EMAIL_NOT_FOUND_MESSAGE, LOGIN_FAIL_MESSAGE, REGISTRATION_SUCCESS_MESSAGE,
    EMAIL_ALREADY_REGISTERED_MESSAGE, PRESS_ENTER_MESSAGE)

def login_flow() -> Client | Employee | None:
    """Flujo de login por consola. 
    Devuelve el usuario autenticado o None."""
    print ("\n🔐 Inicio de sesión (o escriba 'salir' para cancelar)")

    users = load_users()

    while True:  #intentos ilimitados hasta acertar o cancelar
        email = input("Email: ").strip()

        if not email or email.lower() == "salir":
            print(LOGIN_CANCEL_MESSAGE)
            return
        
        if not is_valid_email(email):
            print(INVALID_EMAIL_FORMAT_MESSAGE)
            input(PRESS_ENTER_MESSAGE)
            continue

        user = find_user_by_email(email, users)
        if not user:
            print(EMAIL_NOT_FOUND_MESSAGE)
            input(PRESS_ENTER_MESSAGE)
            continue

        password = input("Contraseña: ").strip()
        if user.check_password(password):
            print(f"\n🔓 Bienvenido/a {user.first_name}")
            return user
        else:
            print(LOGIN_FAIL_MESSAGE)
            input(PRESS_ENTER_MESSAGE)

def register_new_client():
    """Flujo de registro de un nuevo cliente desde menus cliente o empleado"""
    users = load_users()
    name_pattern = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$")

    print("\n📝 Registro de nuevo cliente")
    
    while True:
        first_name = input("Nombre: ").strip()
        if not first_name or not name_pattern.match(first_name):
            print("⚠️ El nombre solo puede contener letras y espacios.")
            continue
        break

    while True:
        last_name = input("Apellido: ").strip()
        if not last_name or not name_pattern.match(last_name):
            print("⚠️ El apellido solo puede contener letras y espacios.")
            continue
        break
    
    while True:
        email = input ("Email (o Enter para cancelar): ").strip()
        if not email or email =="":
            print(LOGIN_CANCEL_MESSAGE)
            return
        if not is_valid_email(email):
            print(INVALID_EMAIL_FORMAT_MESSAGE)
            continue
        if is_email_registered(email, users):
            print(EMAIL_ALREADY_REGISTERED_MESSAGE)
            continue
        break
    
    while True:
        password = input("Contraseña: ").strip()
        if not password:
            print("⚠️ La contraseña no puede estar vacía.")
            continue
        break
    
    new_user = create_user("client", first_name, last_name, email, password)
    users.append(new_user)
    
    save_users(users)
    
    print(REGISTRATION_SUCCESS_MESSAGE)
    input(PRESS_ENTER_MESSAGE)
    
