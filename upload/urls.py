from django.conf.urls import url
from . import views

app_name = 'upload'
urlpatterns = [
    url(r'^app/upload$', views.Uploads.as_view()),
    url(r'^app/filedown$', views.FileDown.as_view()),
    url(r'^app/file/delete$', views.FileDelete.as_view()),
]