from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()


    def __str__(self):
        return self.name
        

class Design(models.Model):
    design_id = models.AutoField
    design_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.design_name