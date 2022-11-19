from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('movie/', views.movie_list),
    path('movie/<int:id>', views.movie_detail),
]
