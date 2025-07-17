from django.db import models


#Contact Users
class ContactUsers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=500)


#About Us
class Header(models.Model):
    image = models.ImageField(upload_to="header/")
    title = models.CharField(max_length=100)
    text = models.TextField()


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)


#Advantages
class Advantages(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Catalog Products
class Catalog(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=100)


#Products
class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)



#Certificate
class CertificateTitle(models.Model):
    title = models.CharField(max_length=100)


class Certification(models.Model):
    title = models.ForeignKey(CertificateTitle, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='certification/')
    description = models.TextField()


#Category
class CategoryTitle(models.Model):
    title = models.CharField(max_length=100)


class Category(models.Model):
    category_title = models.ForeignKey(CategoryTitle, on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")
    image = models.ImageField(upload_to='category/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Contact Us
class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class ContactNumbers(models.Model):
    contact_us = models.ForeignKey(ContactUs, on_delete=models.CASCADE, related_name="numbers")
    number = models.CharField(max_length=100)

#Social
class Social(models.Model):
    contact_us = models.ForeignKey(ContactUs, on_delete=models.CASCADE, related_name="social")
    link = models.URLField()


#News
class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Clients
class ClientsTitle(models.Model):
    title = models.CharField(max_length=100)


class Clients(models.Model):
    title = models.ForeignKey(ClientsTitle, on_delete=models.SET_NULL, null=True, blank=True,related_name="clients")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')

