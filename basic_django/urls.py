from django.urls import path
  
# importing views from views..py
from .views import view_1, view_2, view_3
  
urlpatterns = [
    path('', view_1, name = "template1"),
    path('2/', view_2, name = "template2"),
    path('3/', view_3, name = "template3"),
]