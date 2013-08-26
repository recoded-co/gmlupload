from django.conf.urls.defaults import *
from gmlupload.models import MapFileUpload
from gmlupload.views import UploadedFilesView

urlpatterns = patterns('',
    (r'^gmls/$', UploadedFilesView.as_view(model=MapFileUpload)),
)