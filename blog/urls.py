from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('contact-users', ContactUsersViewSet)
router.register('header', HeaderViewSet)
router.register('about-us', AboutUsViewSet)
router.register('advantages', AdvantagesViewSet)
router.register('catalogs', CatalogViewSet)
router.register('products', ProductViewSet)
router.register('certificate-title', CertificateTitleViewSet)
router.register('certification', CertificationViewSet)
router.register('main-products', ProductsViewSet)
router.register('category-title', CategoryTitleViewSet)
router.register('categories', CategoryViewSet)
router.register('contact-us', ContactUsViewSet)
router.register('contact-numbers', ContactNumbersViewSet)
router.register('news', NewsViewSet)
router.register('clients-title', ClientsTitleViewSet)
router.register('clients', ClientsViewSet)
router.register('social', SocialViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
