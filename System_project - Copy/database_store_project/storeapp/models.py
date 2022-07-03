# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# class Supplier(models.Model):
#     Id = models.BigAutoField(primary_key=True)
#     First_name = models.CharField(max_length=50)
#     Last_name = models.CharField(max_length=50)
#     Company_Address = models.CharField(max_length=150)
#     Phone_number = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.Company_Address




class Patient(models.Model):
    Id = models.BigAutoField(primary_key = True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    Credit_card_Type = models.CharField(max_length=30)
    Credit_card_Number = models.CharField(max_length=100)

    def __str__(self):
        return self.First_name + "  " + self.Last_name


class Product(models.Model):
    Id = models.IntegerField(primary_key=True)
    # Patient_name = models.ForeignKey(Patient , on_delete=models.CASCADE)
    NeededFiles = models.URLField("Click here for product link")
    ProductPictures = models.ImageField(null=True, blank=True, upload_to="images/")

    def __int__(self):
        return self.Id


class ProductDetails(models.Model):
    Detail_number = models.IntegerField(primary_key=True)
    Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Specific_Details = models.TextField(max_length=200)


# class Order(models.Model):
#     Id = models.BigAutoField(primary_key = True)
#     bought_item = models.ForeignKey(Product,on_delete=models.CASCADE)
#     Customer_Id = models.ForeignKey(Customer,on_delete=models.CASCADE)
#     delievry_date = models.DateField()
#     Price = models.CharField(max_length=100)
#     Credit_card_Number = models.CharField(max_length=100)
