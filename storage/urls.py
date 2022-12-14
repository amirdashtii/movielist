from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("movie", views.MovieViewSet, basename='movie')
router.register("actor", views.ActorViewSet)
router.register("director", views.DirectorViewSet)
router.register("writer", views.WriterViewSet)
router.register("lists", views.ListViewSet, basename='lists')


urlpatterns = [
    path('find_movie/', views.find_movie)
]
# URLConf
urlpatterns += router.urls
