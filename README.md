# PROYECTO: TuModeloDeClientesCanale

📚 **Tienda de Historias** es un sistema de gestión de clientes y compras desarrollado en Python. Permite a clientes comprar libros y a empleados gestionar la tienda, usando Programación Orientada a Objetos, archivos y una estructura modular profesional.

---

## 🎯 Objetivo del proyecto

Simular una tienda de libros con dos roles:
- 👤 **Clientes**: se registran, exploran libros, compran y revisan su historial
- 💼 **Empleados**: administran clientes y compras (pedro@tienda.com/pass:admin) 

El sistema demuestra el uso de:
- Clases e herencia (`User`, `Client`, `Employee`)
- Métodos mágicos (`__init__`, `__str__`)
- Archivos `.json` y `.csv`
- Paquetes y módulos
- Flujo interactivo por consola

---

## 🧩 Estructura del proyecto

TuModeloDeClientes_Canale/
│
├── main.py ← Punto de entrada del programa
│
├── core/ ← Lógica de flujo
│ ├── auth.py ← Login y registro de clientes
│ └── menus.py ← Menús para cliente y empleado
│
├── models/ ← Clases del dominio
│ ├── user.py ← User, Client, Employee
│ ├── product.py ← Product
│ └── purchase.py ← Purchase
│
├── services/ ← Funciones lógicas
│ ├── user_service.py ← Crear, autenticar, guardar usuarios
│ ├── product_service.py ← Catálogo de libros
│ └── purchase_service.py ← Registrar y mostrar compras
│
├── utils/ ← Herramientas reutilizables
│ ├── file_handler.py ← Leer y guardar archivos JSON/CSV
│ └── validators.py ← Validación de emails y nombres
│
├── config/ ← Constantes y mensajes
│ ├── constants.py ← Rutas y configuraciones generales
│ └── messages.py ← Textos del sistema
│
├── data/ ← Persistencia
  ├── users.json ← Usuarios registrados
  ├── purchases.json ← Compras realizadas
  └── products.csv ← Catálogo editable

---

## 👤 Funcionalidades por rol

### Cliente
- Registrarse desde el menú inicial
- Iniciar sesión
- Ver catálogo de libros (paginado)
- Comprar libros (con confirmación)
- Ver historial de compras y total gastado

### Empleado
- Iniciar sesión
- Ver catálogo
- Ver clientes registrados
- Registrar nuevos clientes
- Registrar una compra para un cliente
- Ver historial de un cliente
- Ver historial general con total y email de cada cliente

---

## ✅ Validaciones implementadas

- Email con formato válido
- Email no repetido
- Contraseña no vacía
- Nombre y apellido con letras y espacios (con tildes)
- Confirmación de compra limitada a `'s'` o `'n'`
- Reintentos si el ID del producto es incorrecto

---

## ▶️ Cómo ejecutar el programa

1. Asegurate de tener Python 3 instalado
2. Abrí terminal en la carpeta raíz del proyecto
3. Ejecutá:

```bash
python main.py

📦 Entrega:

Proyecto en GitHub: TuModeloDeClientesCanale
