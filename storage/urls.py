from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('movie/', views.movie_list),
    path('movie/<int:id>', views.movie_detail),
    path('actor/', views.actor_list),
    path('actor/<int:id>', views.actor_detail),
    path('director/', views.director_list),
    path('director/<int:id>', views.director_detail),
    path('writer/', views.writer_list),
    path('writer/<int:id>', views.writer_detail),
]
