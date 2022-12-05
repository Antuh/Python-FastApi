import datetime
import uuid
from fa_learn_app.models.product import ProductIn, ProductOut, ProductStorage

def convert_product_storage_to_out(product :ProductStorage) -> ProductOut:
    # Производит конвертацию ProductSrorage --> ProductOut

    tmp_dict :dict = product.dict()
    tmp_dict.pop("secret_token", None)
    return ProductOut(**tmp_dict)

def convert_product_in_to_storage(product :ProductIn) -> ProductStorage:
    # Производит конвертацию ProductIn --> PrductStorage

    tmp_dict :dict = product.dict()
    product_storage = ProductStorage(id = uuid.uuid4(),
                                     created_at = datetime.datetime.now(),
                                     **tmp_dict)
    return product_storage