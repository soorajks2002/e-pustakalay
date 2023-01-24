from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    
    path('genre/', views.homepage_genre, name='homepage_gnere'),
    path('genre/<slug:genre>', views.book_by_genre, name="book_genre"),
    
    path('order/<int:pk>', views.order_book, name='order_book'),
    path('final-order/<int:pk>', views.order_final, name='order_final'),
    
    path('sign-up/', views.signup_page, name='sign_up'),
    path('new-user/', views.new_user, name='new_user'),
    
    path('sign-in/', views.signin, name='sign_in'),
]
