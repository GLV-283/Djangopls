from django.db import models
from django.urls import reverse
from datetime import date


class filmini(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    title = models.CharField(max_length=50, help_text='Enter field documentation')
    id = models.AutoField(primary_key = True)
    tagline = models.TextField()
    overview = models.TextField()
    status = models.CharField(max_length=10,  default='def_error')
    revenue = models.IntegerField()
    #release_date = models.DateTimeField()
    popularity = models.FloatField()
    original_language = models.CharField(max_length=2)
    budget = models.IntegerField()
    runtime = models.IntegerField()
    producer = models.CharField(max_length=10,  default='regista')



    class Meta:
        ordering = ['title']
        db_table = 'filmini'

    def get_absolute_url(self):
        return reverse('filmini-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
