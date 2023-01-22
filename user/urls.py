from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('order/<int:pk>', views.order_book, name='order_book'),
    path('final-order/<int:pk>', views.order_final, name='order_final'),
]
