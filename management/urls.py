from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.newBook, name='new_book'),
    path('book/save-new-book', views.saveNewBook, name='save_new_book'),
    
    path('auth/', views.newAuth, name='new_auth'),
    path('auth/save-new-auth', views.saveNewAuth, name='save_new_auth'),
    
    path('book/<slug:bid>', views.viewBook, name='book_info'),
    path('auth/<slug:aid>', views.viewAuth, name='auth_info'),
]