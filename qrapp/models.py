from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True,null=True)
    address=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    image=models.ImageField(null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url