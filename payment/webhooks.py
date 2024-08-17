import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

@csrf_exempt
def stripe_webhook(request):
    # Получение полезной нагрузки (payload) из тела запроса
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Попытка создания события Stripe на основе полезной нагрузки и сигнатуры
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Недопустимая полезная нагрузка
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Недопустимая подпись
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        
        # Проверяем, что это режим оплаты и статус платежа - "оплачено"
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                # Пытаемся найти заказ по идентификатору клиента
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                # Если заказ не найден, возвращаем ошибку 404
                return HttpResponse(status=404)
            
            # Помечаем заказ как оплаченный
            order.paid = True
            order.save()
    
    return HttpResponse(status=200)
