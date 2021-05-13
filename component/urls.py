from django.urls import path
from .views import index, contact, catalogo, catalogo1, visualizacao, visualizacao1,  realizapedido, pedido, mostrapedido, delete, some_view, filtro
from .views import xls, send_email,formulario, e ,  lojas#, novopedido,query, EmailForm,

urlpatterns=[
path('', index, name='home' ),
path('contact/', contact, name='contact'),
path('catalogo/',catalogo,  name = 'catalogo'),
path('catalogo/produtos/<int:id>', visualizacao, name='visual'),
path('contato/', pedido),
path('realizapedido/', realizapedido, name='pedido'),
path('mostrapedido/', mostrapedido, name='mostrapedido'),
path('mostrapedido/delete/<int:id>', delete, name='delete'),
path('some_view', some_view, name='some_view'),
path('confeitaria/', filtro, name='filtro' ),
########### novo ######### CONFEITARIA
path('catalogo1/',catalogo1,  name = 'catalogo1'),
path('catalogo1/produtos1/<int:id>', visualizacao1, name='visual1'),
path('formulario/', formulario, name='formulario'),
path('xls', xls, name='xls'),
path('email/', e, name='e'),
#path('teste/', novopedido, name="novopedido"),
#path('teste/', query, name='soma'),
path('teste/', lojas, name='lojas'),
#path('mostrapedido/', email, name='email')#add email 2


]
