from django.db import models

class Course(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField( default="Course")
    name= models.CharField(max_length=100)
    video= models.FileField(upload_to='lectures/videos/', null=True, blank=True)
    ebook= models.FileField(upload_to='lectures/notes/')
    image = models.ImageField(upload_to='lectures/images/', null=True, blank=True)
    

    def _str_(self):
        return self.name