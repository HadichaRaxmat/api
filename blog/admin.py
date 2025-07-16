from django.db import models


#Contact Users
class ContactUsers(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.EmailField()


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


#Our Products
class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    last = models.CharField(max_length=100)


class CatalogTitle(models.Model):
    title = models.CharField(max_length=100)


class Catalog(models.Model):
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



