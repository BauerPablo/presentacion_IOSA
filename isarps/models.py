from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ChapterIsarp(models.Model):
    chapter = models.CharField(max_length=50, verbose_name="Capítulo")
    description = models.CharField(max_length=150, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"

    def __str__(self):
        return self.chapter

class Isarp(models.Model):
    title_isarp = models.CharField(max_length=50, verbose_name="Título ISARP")
    content_isarp = RichTextUploadingField(verbose_name="Contenido ISARP")
    slug_isarp = models.CharField(max_length=150, verbose_name="slug ISARP")
    chapters = models.ManyToManyField(ChapterIsarp, verbose_name="Capítulo")
    order_isarp = models.IntegerField(default=0, verbose_name="Orden")
    public_isarp = models.BooleanField(verbose_name="Público")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "ISARP"
        verbose_name_plural = "ISARP's"

    def __str__(self):
        return self.title_isarp

    def previous(self):
        try:
            return Isarp.objects.get(order_isarp=self.order_isarp - 1)
        except:
            return None
        
    def next(self):
        try:
            return Isarp.objects.get(order_isarp=self.order_isarp + 1)
        except:
            return None