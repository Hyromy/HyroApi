from django.db import models

class Guild(models.Model):
    discord_id = models.BigIntegerField(unique = True)
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField()

    def __str__(self):
        return self.name
