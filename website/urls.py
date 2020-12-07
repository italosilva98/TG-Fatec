from django.urls import path
from .views import IndexView, ContatoView, ServicoView, AgendaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('servico/', ServicoView.as_view(), name='servico'),
    path('agenda/', AgendaView.as_view(), name='agenda'),
    path('contato/', ContatoView.as_view(), name='contato'),


]