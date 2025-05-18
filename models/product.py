class Product:
    """Clase que representa un libro disponible en Tienda de Historias"""

    def __init__(self, product_id: str, title: str, author: str, genre: str, price: float) -> None:
        self.product_id = product_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def __str__(self) -> str:
        return f"[{self.product_id}] {self.title} - {self.author} ({self.genre})"
    