from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    # Получаем текущую корзину пользователя
    cart = Cart(request)
    if request.method == 'POST':
        # Если запрос POST, создаем форму с данными из запроса
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Если форма валидна, сохраняем новый заказ
            order = form.save()
            # Для каждого элемента в корзине создаем объект OrderItem
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # Очищаем корзину после создания заказа
            cart.clear()
            # Отображаем страницу с подтверждением создания заказа
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        # Если запрос не POST, создаем пустую форму для нового заказа
        form = OrderCreateForm()
    # Отображаем страницу создания заказа с формой и корзиной
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
