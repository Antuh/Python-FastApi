from typing import List
import uuid
import requests
import random


BASE_URL = "http://localhost:8000/"

def form_data_product() -> dict:
    """Формирование данных продукта"""

    return {
        "name": f"Product {random.randint(0,100000)}",
        "description": f"Description {random.randint(0,100000)}",
        "secret_token": str(uuid.uuid4())
    }

def get_all_products() -> List[dict]:
    """Получение всех продуктов в система"""

    products = requests.get(BASE_URL+"/products")
    return products.json()

def get_product_by_id(id :uuid.UUID) -> dict:
    """Получение продукта по id"""

    product = requests.get(BASE_URL+"/product?id={id}")
    return product.json()