from django.urls import path
from .views import MenuView, IndexView, AboutView, BookTableView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('about/', AboutView.as_view(), name='about'),
    path('book/', BookTableView.as_view(), name='book'),
]
