from django.db import models

class InputText(models.Model):
    input_text = models.CharField(max_length = 256)

