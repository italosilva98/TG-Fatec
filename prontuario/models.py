from django.db import models
from ckeditor.fields import RichTextField


class Base(models.Model):
    created = models.DateTimeField('Cadastro do cliente criado em:', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Paciente(Base):
    CIVIL_CHOICES = [
        ('S', 'Solteira(o)'),
        ('C', 'Casada (o)'),
        ('V', 'Viúva(o)'),
        ('E', 'Em União estável'),
    ]
    ESC_CHOICES = [
        ('in', 'Infantil ou Jardim'),
        ('f1', 'Fundamental Incompleto'),
        ('f2', 'Fundamental Completo'),
        ('m1', 'Médio Incompleto'),
        ('m2', 'Médio Completo'),
        ('s1', 'Superior Incompleto'),
        ('s2', 'Superior Completo'),
        ('p', 'Pós Graduação'),
        ('me', 'Mestre'),
        ('d', 'Doutor'),
        ('pd', 'Pós Doutor'),
    ]
    # Dados Gerais
    nome = models.CharField('Nome completo', max_length=100)
    datanasc = models.DateField('Data de Nascimento', max_length=100)
    cpf = models.CharField('CPF', max_length=100)
    tel = models.CharField('Telefone', max_length=100)
    religiao = models.CharField('Religião', max_length=100)
    estado_civil = models.CharField('Estado civil', choices=CIVIL_CHOICES, blank=True, null=True, max_length=100)
    email = models.EmailField('E-mail', max_length=100, blank=True, null=True)
    endereco = models.CharField('Endereço completo', max_length=100)
    escolaridade = models.CharField('Grau Escolaridade', choices=ESC_CHOICES, blank=True, null=True, max_length=100)
    profissao = models.CharField('Local que trabalha e função', max_length=200, blank=True, null=True)
    contato_recado = models.CharField('Contato para recado/emergencia - Nome e Telefone', max_length=100, blank=True,
                                      null=True)

    # Dados específicos
    motivo_consulta = models.TextField('Quais motivos levaram a buscar a terapia?', max_length=255, blank=True,
                                       null=True)
    outra_consulta = models.CharField('Realizou psicoterapia (com psicólogo) antes? Se sim, por quanto tempo?',
                                      max_length=255, blank=True, null=True)
    acompanhamento = models.CharField(
        'Realiza acompanhamento com médico psiquiatra atualmente? Se sim, há quanto tempo e qual o nome do(a) médico(a)?',
        max_length=255, blank=True, null=True)
    medicamento = models.TextField(
        'Faz uso de alguma medicação? Se sim, qual(is) e há quanto tempo? (Considere aquela de uso frequente ou contínuo, nome da medicação, a dosagem e quem prescreveu) ',
        max_length=255, blank=True, null=True)
    desejo = models.TextField('O que deseja alcaçar com a psicoterapia?', max_length=255, blank=True, null=True)
    aumentar_comport = models.TextField('Quais comportamentos deseja aumentar com a psicoterapia?', max_length=255,
                                        blank=True, null=True)
    diminuir_comport = models.TextField('Quais comportamentos deseja diminuir com a psicoterapia?', max_length=255,
                                        blank=True, null=True)

    class Meta:
        verbose_name = 'Cadastro de Paciente'
        verbose_name_plural = 'Cadastro de Pacientes'

    def __str__(self):
        return self.nome


class Prontuario(Base):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuario_paciente')
    dataconsulta = models.DateField('Data Consulta', auto_now_add=False)
    descricao = RichTextField('Descrição do Atendimento')

    class Meta:
        verbose_name = 'Cadastro de Consulta'
        verbose_name_plural = 'Cadastro de Consultas'

    def __str__(self):
        return self.dataconsulta.strftime('%d/%m/%Y')
