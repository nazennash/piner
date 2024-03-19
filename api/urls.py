from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProductViewSet,  basename='people')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('main_category',views.Show_main_category.as_view()),
    path('new_arrivals',views.NewArrivals.as_view()),
]