
from django.urls import path
from women.views import *
urlpatterns = [

    path('', index),
    path('cats/', cats),

]
