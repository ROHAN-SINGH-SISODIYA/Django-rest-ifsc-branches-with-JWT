from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView

urlpatterns = {
    url(r'^ifsc?$', DetailView.as_view()),
    url(r'^branches?$', ListView.as_view(),name='branchesdetails'),
}

urlpatterns = format_suffix_patterns(urlpatterns)