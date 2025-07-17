from django.urls import path
from .views import *

urlpatterns = [
    path('contact-users/', ContactUsersList.as_view()),
    path('contact-users/create/', ContactUsersCreate.as_view()),
    path('contact-users/<int:pk>/', ContactUsersGet.as_view()),
    path('contact-users/<int:pk>/update/', ContactUsersUpdate.as_view()),
    path('contact-users/<int:pk>/delete/', ContactUsersDelete.as_view()),
    path('header/', HeaderList.as_view()),
    path('header/create/', HeaderCreate.as_view()),
    path('header/<int:pk>/', HeaderGet.as_view()),
    path('header/<int:pk>/update/', HeaderUpdate.as_view()),
    path('header/<int:pk>/delete/', HeaderDelete.as_view()),

    path('aboutus/', AboutUsList.as_view()),
    path('aboutus/create/', AboutUsCreate.as_view()),
    path('aboutus/<int:pk>/', AboutUsGet.as_view()),
    path('aboutus/<int:pk>/update/', AboutUsUpdate.as_view()),
    path('aboutus/<int:pk>/delete/', AboutUsDelete.as_view()),

    path('certification/', CertificationList.as_view()),
    path('certification/create/', CertificationCreate.as_view()),
    path('certification/<int:pk>/', CertificationGet.as_view()),
    path('certification/<int:pk>/update/', CertificationUpdate.as_view()),
    path('certification/<int:pk>/delete/', CertificationDelete.as_view()),

    path('advantages/', AdvantagesList.as_view()),
    path('advantage/create/', AdvantagesCreate.as_view()),
    path('advantage/<int:pk>/', AdvantagesGet.as_view()),
    path('advantage/<int:pk>/update/', AdvantagesUpdate.as_view()),
    path('advantage/<int:pk>/delete/', AdvantagesDelete.as_view()),

    path('products/', ProductsList.as_view()),
    path('products/create/', ProductsCreate.as_view()),
    path('products/<int:pk>/', ProductsGet.as_view()),
    path('products/<int:pk>/update/', ProductsUpdate.as_view()),
    path('products/<int:pk>/delete/', ProductsDelete.as_view()),

    path('category-title/', CategoryTitleList.as_view()),
    path('category-title/create/', CategoryTitleCreate.as_view()),
    path('category-title/<int:pk>/', CategoryTitleGet.as_view()),
    path('category-title/<int:pk>/update/', CategoryTitleUpdate.as_view()),
    path('category-title/<int:pk>/delete/', CategoryTitleDelete.as_view()),

    path('category/', CategoryList.as_view()),
    path('category/create/', CategoryCreate.as_view()),
    path('category/<int:pk>/', CategoryGet.as_view()),
    path('category/<int:pk>/update/', CategoryUpdate.as_view()),
    path('category/<int:pk>/delete/', CategoryDelete.as_view()),

    path('contact-us/', ContactUsList.as_view()),
    path('contact-us/create/', ContactUsCreate.as_view()),
    path('contact-us/<int:pk>/', ContactUsGet.as_view()),
    path('contact-us/<int:pk>/update/', ContactUsUpdate.as_view()),
    path('contact-us/<int:pk>/delete/', ContactUsDelete.as_view()),


    path('news/', NewsList.as_view()),
    path('news/create/', NewsCreate.as_view()),
    path('news/<int:pk>/', NewsGet.as_view()),
    path('news/<int:pk>/update/', NewsUpdate.as_view()),
    path('news/<int:pk>/delete/', NewsDelete.as_view()),

    path('clients-title/', ClientsTitleList.as_view()),
    path('clients-title/create/', ClientsTitleCreate.as_view()),
    path('clients-title/<int:pk>/', ClientsTitleGet.as_view()),
    path('clients-title/<int:pk>/update/', ClientsTitleUpdate.as_view()),
    path('clients-title/<int:pk>/delete/', ClientsTitleDelete.as_view()),

    path('clients/', ClientsList.as_view()),
    path('clients/create/', ClientsCreate.as_view()),
    path('clients/<int:pk>/', ClientsGet.as_view()),
    path('clients/<int:pk>/update/', ClientsUpdate.as_view()),
    path('clients/<int:pk>/delete/', ClientsDelete.as_view()),

    path('catalog/', CatalogList.as_view()),
    path('catalog/create/', CatalogCreate.as_view()),
    path('catalog/<int:pk>/', CatalogGet.as_view()),
    path('catalog/<int:pk>/update/', CatalogUpdate.as_view()),
    path('catalog/<int:pk>/delete/', CatalogDelete.as_view()),

    path('product/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/<int:pk>/', ProductGet.as_view()),
    path('product/<int:pk>/update/', ProductUpdate.as_view()),
    path('product/<int:pk>/delete/', ProductDelete.as_view()),
]
