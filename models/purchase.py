import uuid
from datetime import datetime
from models.product import Product

class Purchase:
    """ Representa una compra hecha por un cliente"""
    def __init__(self, user_email: str, product: Product, date=None, purchase_id=None) -> None:
        self.purchase_id = purchase_id or str(uuid.uuid4())
        self.user_email = user_email # quien compró
        self.product_id = product.product_id
        self.product_title = product.title
        self.price = product.price
        self.date = date or datetime.now().isoformat()

    def __str__(self) -> str:
        return f"{self.date[:10]} - {self.product_title} - (${self.price:.2f})"