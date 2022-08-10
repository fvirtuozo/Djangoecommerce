from django.db import models


class ProductManager(models.manager)
    def get_by_id(self,id):
        qs=self.get_by_id(seld,id)
        if qs.count()==1
            return qs.first
    return None

# Create your models here.
class Product(models.Model): #product_category
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    objects = ProductManager()
    
    #python 3
    def __str__(self):
        return self.title
  
