from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

    
class Gestor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    FUNCAO_CHOICES = (
        ('D', u'Diretor'),
        ('C', u'Coordenador'),
        ('P', u'Professor'),
        ('S', u'Secretario'),
    )
    apelido=models.CharField('Apelido', max_length=70, null=True, blank=True)
    usuario=models.CharField('Usuario', max_length=70, choices=FUNCAO_CHOICES)

    def __str__(self):
        return self.apelido

##----------Sala----------------##
class Sala(models.Model):
    sala=models.CharField('Sala', max_length=2, null=True, blank=True)

    def __str__(self):
        return self.sala
##-----------Aluno--------------###

class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    # Adicionando os campos
    matricula = models.CharField('Matricula', max_length=12)
    foto = models.ImageField(upload_to='pic_aluno/%Y/%m%d', null=True, blank=True)
    nome = models.CharField('Nome', max_length=120)
    serie = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    cpf = models.CharField('CPF',max_length=11, blank=True, null=True)
    email= models.EmailField('Email', max_length=120,blank=False,)
    dataNascimento = models.DateField('Data Nascimento', blank=True, null=True)
    sexo = models.CharField('Sexo',max_length=1, choices=SEXO_CHOICES)
    estadoCivil = models.CharField('Estado Civil', max_length=1, choices=ESTADO_CIVIL_CHOICES)
    TelCelular = models.CharField('Tel. Celular', max_length=11, blank=True, null=True)
    TelFixo = models.CharField('Tel. Fixo', max_length=11, blank=True, null=True)
    #author = models.ForeignKey(Gestor, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now=True,null=True)
   
        
    
    def __str__(self):
        return self.nome


###--------------Professor----------------#
    
class Professor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicionando os campos
    professor = models.CharField('Professor', max_length=70, null=True,blank=True)
    disciplina = models.CharField('Disciplina', max_length=70, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Professor'

    def __str__(self):
        return self.professor

#-------Classe Aluno -----##
