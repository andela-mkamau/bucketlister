from django.db import models


class Timestampable(models.Model):
    '''
    A model mixin that adds date_created and date_modified fields
    '''
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
