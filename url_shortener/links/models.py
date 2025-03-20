from django.db import models
from django.contrib.auth.models import User

class ShortenedLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    name = models.CharField(max_length=15, null=True) #Сокращенная ссылка
    address = models.URLField()  # Полная ссылка

    def __str__(self):
        return f"{self.name} -> {self.address}"