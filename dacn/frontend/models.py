from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
class Website(models.Model):
    site = models.TextField(unique=True, primary_key=True)

    class Meta:
        db_table= 'website'
        verbose_name_plural = 'Websites'
    
    def __str__(self):
        return self.site
    
class Discount(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.TextField()
    product_price = models.TextField()
    product_old_price = models.TextField()
    product_link = models.TextField()
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, to_field='name', db_column='category_name')
    product_site = models.ForeignKey(Website, on_delete=models.CASCADE, null=True, to_field='site', db_column='product_site')
    product_image = models.TextField()
    class Meta:
        db_table = 'discount'
        verbose_name_plural = 'Products'
    
    def __str__(self):
            return self.product_name
    