from django.db import models
from django.contrib.postgres.fields import ArrayField

class Icon(models.Model):
    name = models.CharField(max_length=64)
    tags = ArrayField(models.CharField(max_length=128), blank=True)

    class Meta:
        db_table = "icons"
        verbose_name = "icone"
        verbose_name_plural = "icones"

    def __str__(self):
        return self.name


class IconType(models.Model):
    name = models.CharField(max_length=32)
    extension = models.CharField(max_length=8)

    class Meta:
        db_table = "icon_types"
        verbose_name = "Tipo do icone"
        verbose_name_plural = "Tipos dos icones"

    def __str__(self):
        return self.name


class IconFile(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, related_name='files')
    icon_file = models.FileField(upload_to='/icons')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_extension = models.ForeignKey(IconType, on_delete=models.CASCADE, related_name='files')

    class Meta:
        db_table = "files"
        verbose_name = "arquivo"
        verbose_name_plural = "arquivos"

    def __str__(self):
        return self.icon_file
