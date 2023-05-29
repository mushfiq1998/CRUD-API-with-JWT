from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Test(models.Model):
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2, 
    blank=True, null=True)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products image", 
    blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ForeignKey(
        ProductImage, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def product_handler(sender, instance, **kwargs):
    Test.objects.create(name=instance.name, price=instance.price)
    print('post save called')
    print(instance)
