from django.urls import path, include

from testOne.views import about, index
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
