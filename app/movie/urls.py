"""
URL mappings for the feeling app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie import views
router = DefaultRouter()
router.register('movies',views.MovieViewSet)
# movie movies 이거 기준이모지?
app_name = 'movie'

urlpatterns = [
    path('', include(router.urls))
]