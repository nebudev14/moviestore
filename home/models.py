from django.db import models
from django.contrib.auth.models import User

class SecurityPhrase(models.Model):
    id = models.AutoField(primary_key=True)
    phrase = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.phrase
