from django.urls import path, include
from . import views
from django.contrib import admin
#from django.urls import path
#from . import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#
# ]

urlpatterns = [
     path('admin/', admin.site.urls),
  

    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('ex1', views.ex1, name='ex1'),
    
]