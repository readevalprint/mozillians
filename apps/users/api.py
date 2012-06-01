from django.template.loader import render_to_string
from django.template import RequestContext
from datetime import datetime

from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from users.models import UserProfile


class VouchedAuthentication(Authentication):
    """
    Api Authentication that only lets in authenticated and vouched users.
    """
    def is_authenticated(self, request, **kwargs):
        user = request.user
        if user.is_authenticated() and user.get_profile().is_vouched:
            return True

        return False

    def get_identifier(self, request):
        return request.user.username


class UserSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'html']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'html': 'text/html',
    }

    def to_html(self, data, options=None):
        return render_to_string('api.html', locals())


class UserProfileResource(ModelResource):
    email = fields.CharField(attribute='email', null=True, readonly=True)

    class Meta:
        queryset = UserProfile.objects.select_related()
        authentication = VouchedAuthentication()
        authorization = ReadOnlyAuthorization()
        serializer = UserSerializer()
        resource_name = 'users'
        fields = ['display_name', 'id', 'website', 'ircname', 'last_updated']

    def get_object_list(self, request):
        if 'updated' in request.GET:
            try:
                time = datetime.fromtimestamp(int(request.GET.get('updated')))
            except TypeError:
                pass
            else:
                return (super(UserProfileResource, self)
                        .get_object_list(request)
                        .filter(last_updated__gt=time))

        return super(UserProfileResource, self).get_object_list(request)
