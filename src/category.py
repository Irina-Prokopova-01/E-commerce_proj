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

    def __str__(self):
        # total_quantity = 0
        # for item in self.__products:
        #     total_quantity += item.quantity
        # return f"{self.name}, количество продуктов: {total_quantity} шт."
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"

        return product_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            total_price = 0
            total_quantity = 0
            for product in self.__products:
                total_price += product.price * product.quantity
                total_quantity += product.quantity
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0
