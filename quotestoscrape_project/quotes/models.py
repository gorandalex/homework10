from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField()
    born_location = models.CharField()
    born_description = models.CharField()
    
    def __str__(self) -> str:
        return self.fullname
    
class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.CharField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.quote
    
    
