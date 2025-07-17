from rest_framework import serializers
from .models import *


class ContactUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsers
        fields = ['id', 'name', 'email', 'message']



class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'image', 'title', 'text', 'last']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'image', 'title', 'text']


class CertificateTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateTitle
        fields = ['id', 'title']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'image', 'description']


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['id', 'title', 'description']



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'image', 'title', 'text', 'last']


class CategoryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTitle
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'image', 'title', 'description']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'email', 'location']



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'title', 'description']


class ClientsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsTitle
        fields = ['id', 'title']


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'name', 'image']


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'title']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'description']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'link']


class ContactNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumbers
        fields = ['id', 'number']