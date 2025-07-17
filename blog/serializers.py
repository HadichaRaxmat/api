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


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'image', 'description']


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['id', 'title']


class AdvantageMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantageMenu
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
        fields = ['id', 'email', 'phone', 'location']


class NewsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTitle
        fields = ['id', 'title']


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


class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCategory
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'description']
