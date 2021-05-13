from django.urls import path
from . import views
#from .views import index, contact, catalogo, visualizacao,  realizapedido, pedido

urlpatterns=[

    path('register/', views.SignUp.as_view(), name="signup"),

]
