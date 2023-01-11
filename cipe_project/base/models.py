from django.db import models

# Create your models here.
class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    conversation_id = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
