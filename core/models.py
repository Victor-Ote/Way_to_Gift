from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    modified_at = models.DateTimeField('modified at', auto_now=True)
    
    class Meta:
        abstract = True
        
class Category(Base):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Gift(Base):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    reference_url = models.URLField(blank=True)
    preference_date = models.DateField(null=True, blank=True, default=None)
    was_purchased = models.BooleanField(default=False)
    
    def __str__(self):
       return self.name
    