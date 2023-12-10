from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return f'[{self.id}] {self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)
