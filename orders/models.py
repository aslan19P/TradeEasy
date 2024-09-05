
# Create your models here.
from django.db import models
from products.models import Product

class Order(models.Model):
    # Имя покупателя
    first_name = models.CharField(max_length=50)
    # Фамилия покупателя
    last_name = models.CharField(max_length=50)
    # Электронная почта покупателя
    email = models.EmailField()
    # Адрес доставки
    address = models.CharField(max_length=250)
    # Почтовый индекс
    postal_code = models.CharField(max_length=20)
    # Город доставки
    city = models.CharField(max_length=100)
    # Дата и время создания заказа (автоматически заполняется при создании)
    created = models.DateTimeField(auto_now_add=True)
    # Дата и время последнего обновления заказа (автоматически обновляется при изменении)
    updated = models.DateTimeField(auto_now=True)
    # Статус оплаты заказа (по умолчанию False, т.е. не оплачено)
    paid = models.BooleanField(default=False)

    class Meta:
        # Сортировка по дате создания в обратном порядке (от новых к старым)
        ordering = ['-created']
        # Индекс по полю created для оптимизации запросов
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        # Строковое представление объекта заказа
        return f'Order {self.id}'

    def get_total_cost(self):
        # Расчет общей стоимости заказа
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    # Связь с заказом (каждый элемент привязан к определенному заказу)
    order = models.ForeignKey(
        Order,
        related_name='items',  # Позволяет получать все элементы для конкретного заказа через order.items
        on_delete=models.CASCADE  # При удалении заказа удаляются все связанные элементы
    )
    # Связь с продуктом (каждый элемент связан с конкретным продуктом)
    product = models.ForeignKey(
        Product,
        related_name='order_items',  # Позволяет получать все элементы заказа для конкретного продукта
        on_delete=models.CASCADE  # При удалении продукта удаляются все связанные элементы заказа
    )
    # Цена продукта на момент добавления в заказ
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Количество продукта в заказе
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        # Строковое представление объекта элемента заказа
        return str(self.id)

    def get_cost(self):
        # Возвращает общую стоимость для данного элемента (цена * количество)
        return self.price * self.quantity
