import uuid
from datetime import datetime

class User:
    """Clase general para usuarios del sistema
    Incluye atributos comunes y métodos compartidos"""

    def __init__(self, user_id: str, first_name: str, last_name: str, email: str, password: str, role: str, registration_date) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role                # Cliente o Empleado
        self.registration_date = registration_date or datetime.now()

    def check_password(self, input_password: str) -> bool:
        """Verifica si la contraseña ingresada coincide con la registrada."""
        return self.password == input_password

    def __str__(self) -> str:
        return f"[{self.role.upper()}] {self.first_name} {self.last_name} <{self.email}>"   
    
class Client(User):         # Uso de HERENCIA
    """Usuario con rol de cliente (se asigna role = "client")"""

    def __init__(self, user_id: str, first_name: str, last_name: str, email: str, password: str, registration_date, role="client") -> None:
        super().__init__(user_id,first_name, last_name, email, password, role, registration_date)
        self.purchase_history = [] # Lista de compras

    def __str__(self) -> str:
        fecha = self.registration_date.strftime('%d/%m/%Y')
        return f"{self.first_name} {self.last_name} - {self.email} (Registrado el {fecha})"

class Employee(User):        # Uso de HERENCIA
    """Usuario con rol de empleado (se asigna role = "employee")"""

    def __init__(self,user_id: str, first_name: str, last_name: str, email: str, password: str, registration_date, role="employee") -> None:
        super().__init__(user_id,first_name, last_name, email, password, role, registration_date=registration_date)