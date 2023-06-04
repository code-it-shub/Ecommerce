from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('products/', views.productsView.as_view()),
    path('users/',views.userView.as_view())
]
