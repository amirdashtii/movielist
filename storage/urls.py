from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("movie", views.MovieViewSet, basename='movie')
router.register("actor", views.ActorViewSet)
router.register("director", views.DirectorViewSet)
router.register("writer", views.WriterViewSet)
router.register("lists", views.ListViewSet, basename='lists')

# URLConf
urlpatterns = router.urls
