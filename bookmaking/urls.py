from django.conf.urls import url
from . import views
from bookmaking.views import user_view

urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^user/$', user_view.as_view()),
]