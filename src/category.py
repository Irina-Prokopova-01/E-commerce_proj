from src.product import Product


class Category:
    """Класс представления категории продуктов."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    @property
    def products(self):
        return self.__products

    @products.setter
    def add_product(self, product: Product):
        self.__products = []
        self.__products.append(product)
        Category.product_count += 1


    @property
    def get_product(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."

        return product_str
