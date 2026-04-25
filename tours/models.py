from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name