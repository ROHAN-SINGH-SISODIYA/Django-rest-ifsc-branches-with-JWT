#fyleHQ URL Configuration

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import CustomLoginView

urlpatterns = [
    url(r'^', include('api.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
]
