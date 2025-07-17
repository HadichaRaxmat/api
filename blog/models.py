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
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=100)


#Certificate
class CertificateTitle(models.Model):
    title = models.CharField(max_length=100)


class Certification(models.Model):
    image = models.ImageField(upload_to='certification/')
    description = models.TextField()


#Products
class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)


class CategoryTitle(models.Model):
    title = models.CharField(max_length=100)


class Category(models.Model):
    image = models.ImageField(upload_to='category/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Contact Us
class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class ContactNumbers(models.Model):
    number = models.CharField(max_length=100)


#News
class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Clients
class ClientsTitle(models.Model):
    title = models.CharField(max_length=100)


class Clients(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')

#Social
class Social(models.Model):
    link = models.URLField()