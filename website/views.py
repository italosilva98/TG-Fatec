
from django.views.generic import TemplateView
from .models import Service, PaginaIndex, Contato
from .forms import ContatoForm



class IndexView(TemplateView):
    template_name = 'index.html' 

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['index'] = PaginaIndex.objects.all()
        context['contatos'] = Contato.objects.all()
        return context

class ServicoView(TemplateView):
    template_name = 'servico.html'

    def get_context_data(self, **kwargs):
        context = super(ServicoView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['contatos'] = Contato.objects.all()
        return context


class AgendaView(TemplateView):
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)
        context['contatos'] = Contato.objects.all()
        return context

class ContatoView(TemplateView):
    template_name = 'contato.html'
    
    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        context['contatos'] = Contato.objects.all()
        return context    

    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail sent successfully')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'E-mail sent failed')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
