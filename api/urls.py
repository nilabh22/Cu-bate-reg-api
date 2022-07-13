from django.urls import path
from . import views


urlpatterns = [
    path('api/register', views.api, name = 'api'),
    #path('update/<int:pk>/', views.updatePayment, name = 'updatePaymentStatus')
]