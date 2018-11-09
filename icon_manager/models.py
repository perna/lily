import string

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Icon(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=64, unique=True)
    tags = ArrayField(models.CharField(max_length=128), blank=True)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True)

    class Meta:
        db_table = "icons"
        verbose_name = "icone"
        verbose_name_plural = "icones"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'details/{}'.format(self.slug)



class IconFile(models.Model):
    # file formats
    AI = 'AI'
    EPS = 'EPS'
    JPG = 'JPG'
    PDF = 'PDF'
    PNG = 'PNG'
    SVG = 'SVG'

    filetype_choices = (
        (AI, 'ai'),
        (EPS, 'eps'),
        (JPG, 'jpg'),
        (PDF, 'pdf'),
        (PNG, 'png'),
        (SVG, 'svg')
    )

    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, related_name='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_extension = models.CharField(verbose_name='Formato', max_length=4, choices=filetype_choices, default=SVG)
    icon_file = models.FileField(verbose_name='Arquivo', upload_to='icons/')

    class Meta:
        db_table = "files"
        verbose_name = "arquivo"
        verbose_name_plural = "arquivos"
