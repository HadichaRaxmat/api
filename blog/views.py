from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *


class ContactUsersList(APIView):
    def get(self, request):
        data = ContactUsers.objects.all()
        serializer = ContactUsersSerializer(data, many=True)
        return Response(serializer.data)

class ContactUsersCreate(APIView):
    def post(self, request):
        serializer = ContactUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsersGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(ContactUsers, pk=pk)
        serializer = ContactUsersSerializer(obj)
        return Response(serializer.data)

class ContactUsersUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(ContactUsers, pk=pk)
        serializer = ContactUsersSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsersDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(ContactUsers, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoList(APIView):
    def get(self, request):
        data = Logo.objects.all()
        serializer = LogoSerializer(data, many=True)
        return Response(serializer.data)

class LogoCreate(APIView):
    def post(self, request):
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Logo, pk=pk)
        serializer = LogoSerializer(obj)
        return Response(serializer.data)

class LogoUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Logo, pk=pk)
        serializer = LogoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Logo, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuList(APIView):
    def get(self, request):
        data = Menu.objects.all()
        serializer = MenuSerializer(data, many=True)
        return Response(serializer.data)

class MenuCreate(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(obj)
        return Response(serializer.data)

class MenuUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Menu, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MainPageList(APIView):
    def get(self, request):
        data = MainPage.objects.all()
        serializer = MainPageSerializer(data, many=True)
        return Response(serializer.data)

class MainPageCreate(APIView):
    def post(self, request):
        serializer = MainPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MainPageGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(MainPage, pk=pk)
        serializer = MainPageSerializer(obj)
        return Response(serializer.data)

class MainPageUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(MainPage, pk=pk)
        serializer = MainPageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MainPageDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(MainPage, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutUsList(APIView):
    def get(self, request):
        data = AboutUs.objects.all()
        serializer = AboutUsSerializer(data, many=True)
        return Response(serializer.data)

class AboutUsCreate(APIView):
    def post(self, request):
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutUsGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(AboutUs, pk=pk)
        serializer = AboutUsSerializer(obj)
        return Response(serializer.data)

class AboutUsUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(AboutUs, pk=pk)
        serializer = AboutUsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutUsDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(AboutUs, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CertificationList(APIView):
    def get(self, request):
        data = Certification.objects.all()
        serializer = CertificationSerializer(data, many=True)
        return Response(serializer.data)

class CertificationCreate(APIView):
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Certification, pk=pk)
        serializer = CertificationSerializer(obj)
        return Response(serializer.data)

class CertificationUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Certification, pk=pk)
        serializer = CertificationSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Certification, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AdvantageList(APIView):
    def get(self, request):
        data = Advantage.objects.all()
        serializer = AdvantageSerializer(data, many=True)
        return Response(serializer.data)

class AdvantageCreate(APIView):
    def post(self, request):
        serializer = AdvantageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvantageGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Advantage, pk=pk)
        serializer = AdvantageSerializer(obj)
        return Response(serializer.data)

class AdvantageUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Advantage, pk=pk)
        serializer = AdvantageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvantageDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Advantage, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdvantageMenuList(APIView):
    def get(self, request):
        data = AdvantageMenu.objects.all()
        serializer = AdvantageMenuSerializer(data, many=True)
        return Response(serializer.data)

class AdvantageMenuCreate(APIView):
    def post(self, request):
        serializer = AdvantageMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvantageMenuGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(AdvantageMenu, pk=pk)
        serializer = AdvantageMenuSerializer(obj)
        return Response(serializer.data)

class AdvantageMenuUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(AdvantageMenu, pk=pk)
        serializer = AdvantageMenuSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvantageMenuDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(AdvantageMenu, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsList(APIView):
    def get(self, request):
        data = Products.objects.all()
        serializer = ProductsSerializer(data, many=True)
        return Response(serializer.data)

class ProductsCreate(APIView):
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(obj)
        return Response(serializer.data)

class ProductsUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Products, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryTitleList(APIView):
    def get(self, request):
        data = CategoryTitle.objects.all()
        serializer = CategoryTitleSerializer(data, many=True)
        return Response(serializer.data)

class CategoryTitleCreate(APIView):
    def post(self, request):
        serializer = CategoryTitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryTitleGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(CategoryTitle, pk=pk)
        serializer = CategoryTitleSerializer(obj)
        return Response(serializer.data)

class CategoryTitleUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(CategoryTitle, pk=pk)
        serializer = CategoryTitleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryTitleDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(CategoryTitle, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request):
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

class CategoryCreate(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(obj)
        return Response(serializer.data)

class CategoryUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Category, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactUsList(APIView):
    def get(self, request):
        data = ContactUs.objects.all()
        serializer = ContactUsSerializer(data, many=True)
        return Response(serializer.data)

class ContactUsCreate(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(ContactUs, pk=pk)
        serializer = ContactUsSerializer(obj)
        return Response(serializer.data)

class ContactUsUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(ContactUs, pk=pk)
        serializer = ContactUsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(ContactUs, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsTitleList(APIView):
    def get(self, request):
        data = NewsTitle.objects.all()
        serializer = NewsTitleSerializer(data, many=True)
        return Response(serializer.data)

class NewsTitleCreate(APIView):
    def post(self, request):
        serializer = NewsTitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsTitleGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(NewsTitle, pk=pk)
        serializer = NewsTitleSerializer(obj)
        return Response(serializer.data)

class NewsTitleUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(NewsTitle, pk=pk)
        serializer = NewsTitleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsTitleDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(NewsTitle, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class NewsList(APIView):
    def get(self, request):
        data = News.objects.all()
        serializer = NewsSerializer(data, many=True)
        return Response(serializer.data)

class NewsCreate(APIView):
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(obj)
        return Response(serializer.data)

class NewsUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(News, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientsTitleList(APIView):
    def get(self, request):
        data = ClientsTitle.objects.all()
        serializer = ClientsTitleSerializer(data, many=True)
        return Response(serializer.data)

class ClientsTitleCreate(APIView):
    def post(self, request):
        serializer = ClientsTitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientsTitleGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(ClientsTitle, pk=pk)
        serializer = ClientsTitleSerializer(obj)
        return Response(serializer.data)

class ClientsTitleUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(ClientsTitle, pk=pk)
        serializer = ClientsTitleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientsTitleDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(ClientsTitle, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientsList(APIView):
    def get(self, request):
        data = Clients.objects.all()
        serializer = ClientsSerializer(data, many=True)
        return Response(serializer.data)

class ClientsCreate(APIView):
    def post(self, request):
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientsGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Clients, pk=pk)
        serializer = ClientsSerializer(obj)
        return Response(serializer.data)

class ClientsUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Clients, pk=pk)
        serializer = ClientsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientsDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Clients, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CatalogList(APIView):
    def get(self, request):
        data = Catalog.objects.all()
        serializer = CatalogSerializer(data, many=True)
        return Response(serializer.data)

class CatalogCreate(APIView):
    def post(self, request):
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Catalog, pk=pk)
        serializer = CatalogSerializer(obj)
        return Response(serializer.data)

class CatalogUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Catalog, pk=pk)
        serializer = CatalogSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Catalog, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CatalogCategoryList(APIView):
    def get(self, request):
        data = CatalogCategory.objects.all()
        serializer = CatalogCategorySerializer(data, many=True)
        return Response(serializer.data)

class CatalogCategoryCreate(APIView):
    def post(self, request):
        serializer = CatalogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogCategoryGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(CatalogCategory, pk=pk)
        serializer = CatalogCategorySerializer(obj)
        return Response(serializer.data)

class CatalogCategoryUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(CatalogCategory, pk=pk)
        serializer = CatalogCategorySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogCategoryDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(CatalogCategory, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):
    def get(self, request):
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductGet(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(obj)
        return Response(serializer.data)

class ProductUpdate(APIView):
    def put(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDelete(APIView):
    def delete(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
