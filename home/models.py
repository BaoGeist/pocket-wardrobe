from turtle import color
from django.db import models
from PIL import Image
from . import backend

# Create your models here.
'''
def calcColour():
    return colour

def calcArticle():
    return article
'''



class Wardrobe(models.Model):
    clothing = models.ImageField(null=True, blank=True, upload_to='images', default='defalt.png') #default=?
    colour = models.CharField(max_length=200, default='blue')
    article = models.CharField(max_length=100, default='pants')

    def __str__(self):
        return self.colour #This determines what is shown when query

    def save(self):
        super().save()
        img_path = r'{}'.format(self.clothing.path)
        print(img_path)
        self.colour = backend.process_colour(img_path)
        self.article = backend.getArticle(img_path)
        super().save()
        #self.article = backend.getArticle(img_path)

        
        '''
        img = Image.open(self.clothing.path)
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.clothing.path)
        '''