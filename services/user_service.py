from models.user import Client, Employee
from utils.file_handler import load_json, save_json
from config.constants import USER_FILE
from typing import Literal      #para restringir el valor del parametro "role" a 2 opciones especificas: "client" o "employee"
from datetime import datetime
from uuid import uuid4

def load_users() -> list[Client | Employee]:
    """Carga usuarios desde archivo JSON como objetos Client o Employee."""
    raw_users = load_json(USER_FILE)
    users = []
    for data in raw_users:
        if data["role"] == "client":
            user = Client(
                user_id=data["user_id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                registration_date = datetime.fromisoformat(data["registration_date"]),
                role="client"
            )
        elif data["role"] == "employee":
            user = Employee(
                user_id=data["user_id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                registration_date = datetime.fromisoformat(data["registration_date"]),
                role="employee"
            )
        else:
            print("Rol no existe")
            continue # Ignora si no es un rol valido
        users.append(user)
    return users

def save_users(users: list) ->None:
    """Guarda listas de objetos Client/Employee como diccionarios JSON."""
    raw_data =[]
    for u in users:
        raw_data.append({
            "user_id":u.user_id,
            "first_name": u.first_name,
            "last_name": u.last_name,
            "email": u.email,
            "password": u.password,
            "role": u.role,
            "registration_date": u.registration_date.isoformat()
        })
    save_json(raw_data, USER_FILE)

def create_user(role: Literal["client", "employee"], first_name: str, last_name:str, email: str, password: str):
    """Crea un nuevo usuario segun el rol y lo devuelve
       Valida el formato de email"""
    user_id = str(uuid4())
    registration_date = datetime.now()

    if role == "client":
        return Client(user_id,first_name, last_name, email, password,registration_date)
    elif role == "employee":
        return Employee(user_id,first_name, last_name, email, password,registration_date)
    else:
        raise ValueError("Rol inválido.")
    
def find_user_by_email(email:str, users: list[Client| Employee]):
    """Busca un usuario por email dentro de una lista. 
       Devuelve el objeto o None"""  
    for user in users:
        if user.email == email:
            return user    
    return None


def is_email_registered(email:str, users: list[Client | Employee]) -> bool:
    """Verifica si el email ya está registrado en la lista de usuarios"""
    return any(u.email == email for u in users) #Devuelve True si un usuario tiene el email ingresado

def authenticate_user(email:str, password:str, users: list[Client | Employee]):
    """Devuelve el usuario si el email y la contraseña coinciden, None si falla"""
    user = find_user_by_email(email, users)
    if user and user.check_password(password):
        return user
    return None


