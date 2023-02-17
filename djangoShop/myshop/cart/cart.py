from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        :param request:
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # В сессии сохраняем Пустую Корзину
            cart = self.session[settings.CART_SESSION_ID]
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить Товар в Корзину или Обновить Его Количество.
        :param product:
        :param quantity:
        :param update_quantity:
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновляем сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Помечаем сеанс как "Измененный", для
        # Подтверждения сохранения Сеанса.
        self.session.modified = True

    def remove(self, product):
        """
        Удаление Товара из Корзины.
        :param product:
        :return:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор Элементов в Корзине и
        Получение Продуктов из БД
        :return:
        """
        product_ids = self.cart.keys()
        # Получение Обьектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет Всех Товаров в Корзине.
        :return:
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет Стоимости Товаров в корзине
        :return:
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Удаление корзины Из Сессии.
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
