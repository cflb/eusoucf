from django.urls import path
from .views import website, contato

urlpatterns = [
    path('', website, name='website'),
    path('contato/', contato, name='contato')
]