from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField("Категория", max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"