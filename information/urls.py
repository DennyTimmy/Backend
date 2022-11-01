from django.urls import path
from .views import informationApiView

urlpatterns = [

    path('information/<pk>', informationApiView.as_view()),
]