from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('payment/', include('payment.urls', namespace='payment')),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('products.urls', namespace='products')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
