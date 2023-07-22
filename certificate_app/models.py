import uuid
from django.db import models

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class VerificationToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='verification_tokens')

