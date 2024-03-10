from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('second/ ', views.adress, name='second'),
    path('categ/<int:catid>/', views.categ, name='categ'),

]