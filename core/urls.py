from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('<int:textid>', views.main, name='main'),
    path('add_text', views.add_text, name='add_text'),
    path('my_texts', views.my_texts, name='my_texts'),
    path('edit_text/<textid>', views.edit_text, name='edit_text'),
    path('delete_text/<textid>', views.delete_text, name='delete_text'),
]
