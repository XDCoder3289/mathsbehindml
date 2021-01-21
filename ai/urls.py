from django.urls import path
from ai import views

app_name = 'ai'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_name_slug>/', views.cat, name='cat'),
    path('<slug:category_name_slug>/<slug:post_name_slug>/', views.post, name='post'),
]

