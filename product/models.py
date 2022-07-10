from django.db import models
from django.utils.translation import gettext as _

class Product(models.Model):
    ean = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=30, choices=(
        ('00', _('Not specified')),
        ('10', _('Smoke')),
        ('20', _('Drinks')),
        ('30', _('Foods')),
        ('40', _('Perfumes and Cosmetics')),
        ('50', _('Watches Jewelry & Accessories')),
        ('60', _('Toys')),
        ('70', _('Fashion')),
        ('80', _('Electronics')),
        ('90', _('Other Goods')),
        ('91', _('Readings and Publications')),
        ('92', _('Souvenirs (Local Goods)'))
    ))
    
    
    
    

