from django.db import models

class Base(models.Model):
    created = models.DateTimeField('Criação', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('fa fa-street-view', 'Pessoa'),
    )
    title = models.CharField('Titulo do Serviço', max_length=100)
    description = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=17, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title


class PaginaIndex(Base):
    title = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=400)
    image = models.CharField('Url da Imagem', max_length=400)


    class Meta:
        verbose_name = 'Itens Página Index'
        verbose_name_plural = 'Itens Página Index'

    def __str__(self):
        return self.title


class Contato(Base):
    telefone1 = models.CharField('Telefone', max_length=100)
    telefone2 = models.CharField('WhatsApp', max_length=100)
    email = models.EmailField('E-mail', max_length=250)
    skype = models.CharField('Link Skype', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)

    class Meta:
        verbose_name = 'Informações de Contato'
        verbose_name_plural = 'Informações de Contato'

    def __str__(self):
        return self.email
