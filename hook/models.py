from django.db import models

# Create your models here.


class stock(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'stock'