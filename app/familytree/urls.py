from django.urls import path
from .views import ViewParent, ViewChild, ViewOffspring, ViewMommyDaddy

urlpatterns = [
    path('parent/', ViewParent.as_view()),
    path('children/', ViewChild.as_view()),
    path('offspring/', ViewOffspring.as_view()),
    path('mommydaddy/', ViewMommyDaddy.as_view()),
]
