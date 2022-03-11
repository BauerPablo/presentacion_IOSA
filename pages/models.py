from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Chapter(models.Model):
    chapter = models.CharField(max_length=50, verbose_name="Capítulo")
    description = models.CharField(max_length=150, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"

    def __str__(self):
        return self.chapter

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    content = RichTextUploadingField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="Slug")
    chapters = models.ManyToManyField(Chapter, verbose_name="Capítulo")
    order = models.IntegerField(default=0, verbose_name="Orden")
    public = models.BooleanField(verbose_name="Público")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
    
    def __str__(self):
        return self.title
    