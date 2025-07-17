from rest_framework import viewsets
from .serializers import *


class ContactUsersViewSet(viewsets.ModelViewSet):
    queryset = ContactUsers.objects.all()
    serializer_class = ContactUsersSerializer


class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AdvantagesViewSet(viewsets.ModelViewSet):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CertificateTitleViewSet(viewsets.ModelViewSet):
    queryset = CertificateTitle.objects.all()
    serializer_class = CertificateTitleSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CategoryTitleViewSet(viewsets.ModelViewSet):
    queryset = CategoryTitle.objects.all()
    serializer_class = CategoryTitleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactNumbersViewSet(viewsets.ModelViewSet):
    queryset = ContactNumbers.objects.all()
    serializer_class = ContactNumberSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ClientsTitleViewSet(viewsets.ModelViewSet):
    queryset = ClientsTitle.objects.all()
    serializer_class = ClientsTitleSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
