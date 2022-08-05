from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='publicado')

class Category(models.Model):
    nome = models.CharField(max_length=100)
    published = models.DateField(default=timezone.now)
    create    = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-create']

    def __str__(self):
        return self.nome

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    title = models.CharField(verbose_name="Título",max_length=250)
    slug  = models.SlugField(max_length=250)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)

    categoria = models.ManyToManyField(Category,related_name="get_posts")
    imagem    = models.ImageField(upload_to="blog", blank=True, null=True)
    content   = RichTextField(verbose_name="Conteúdo")
    published = models.DateField(default=timezone.now)
    create    = models.DateTimeField(auto_now_add=True)
    altered   = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                               choices=STATUS,
                               default='rascunho')

    objects   = models.Manager()
    publicado = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('post_delete', args=[self.slug])


    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.imagem.url)
        view_image.short_description = "Imagem Cadastrada"
        view_image.allow_tags = True

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print('Creating slug')

    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()

# Create your models here.
"""

Post.objects.bulk_create([
... Post(title='Testando o bulk do Django 1',slug='testando-o-bulk-do-django-1',content='Testando o bulk do Django 1',autor=user)
... Post(title='Testando o bulk do Django 2',slug='testando-o-bulk-do-django-2',content='Testando o bulk do Django 2',autor=user)
... Post(title='Testando o bulk do Django 23',slug='testando-o-bulk-do-django-3',content='Testando o bulk do Django 3',autor=user)
])
"""