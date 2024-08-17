from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from orders.models import Order

# Создание экземпляра Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    # Получение ID заказа из сессии
    order_id = request.session.get('order_id', None)
    
    # Получение объекта заказа или возвращение ошибки 404, если не найден
    order = get_object_or_404(Order, id=order_id)
    
    # Управление платежами и заказами
    if request.method == 'POST':
        # Создание URL для успешной оплаты и отмены оплаты
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        
        # Данные для сеанса оформления платежа Stripe
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []  # Добавьте сюда элементы заказа
        }
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),  # Преобразование цены в центы
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,  # Название продукта
                    },
                },
                'quantity': item.quantity,  # Количество товара
            }) 
        # Создание сеанса оформления платежа Stripe
        session = stripe.checkout.Session.create(**session_data)
        
        # Перенаправление к платежной форме Stripe
        return redirect(session.url, code=303)
    else:
        # Отображение страницы с процессом оплаты
        return render(request, 'payment/process.html', locals())

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')