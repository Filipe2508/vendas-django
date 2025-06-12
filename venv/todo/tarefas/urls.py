from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet, UsuarioViewSet, VendaSaidaViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'tarefas', TarefaViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'vendas', VendaSaidaViewSet)

urlpatterns = [
    path('listartarefas', views.listarTarefas),
    path('listarusuarios', views.listarUsuarios),
    path('cadastroAtividade', views.cadastroAtividade),
    path('cadastroUsuario', views.cadastroUsuario),
    path('excluirAtividade/<int:id>', views.excluirAtividade),
    path('editarAtividade/<int:id>', views.editarAtividade),
    path('cadastroVenda', views.registrar_venda, name='registrar_venda'),
    path('listarVendas/', views.listarVendas, name='listar_vendas'),
    path('login', views.formlogin),
    path('logout', views.logout_view),
    path('', include(router.urls)),
]

urlpatterns += router.urls