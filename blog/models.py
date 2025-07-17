from django.db import models


#Contact Users
class ContactUsers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=500)


#Logo
class Logo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#Menu
class Menu(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


#About Us
class MainPage(models.Model):
    image = models.ImageField(upload_to="mainpage/")
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    last = models.CharField(max_length=100)


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/')
    main = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    last = models.CharField(max_length=100)


class Certification(models.Model):
    image = models.ImageField(upload_to='certification/')
    description = models.TextField()


#Advantages
class Advantage(models.Model):
    title = models.CharField(max_length=100)


class AdvantageMenu(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Category
class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    last = models.CharField(max_length=100)


class CategoryTitle(models.Model):
    title = models.CharField(max_length=100)


class Category(models.Model):
    image = models.ImageField(upload_to='category/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#Contact Us
class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


#News
class NewsTitle(models.Model):
    title = models.CharField(max_length=100)


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


#Catalog Products
class Catalog(models.Model):
    title = models.CharField(max_length=100)


class CatalogCategory(models.Model):
    name = models.CharField(max_length=100)


#Products
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=100)
