from django.http import HttpResponse
from django.views.generic import ListView
from django.core import serializers
from django.utils import simplejson as json

from gmlupload.models import MapFileUpload


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps([x.to_dict() for x in context['object_list']])
        
        
class UploadedFilesView(JSONResponseMixin, ListView):
    pass

