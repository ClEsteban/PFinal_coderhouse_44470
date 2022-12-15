from django.db import models
from django.contrib.auth.models import User


class Mensajes(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    msg_content = models.TextField()
    fecha = models.DateTimeField()
    def __str__(self):
        return '{}-{}'.format(self.sender,self.fecha) 