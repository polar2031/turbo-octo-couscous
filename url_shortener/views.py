import json
import random
import string

from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import UrlMappingTable


class UrlView(View):
    # redirect to matching url
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, id=None):
        if not id:
            return render(request, template_name='index.html')
        object = get_object_or_404(UrlMappingTable, pk=id)
        return redirect(object.url)

    # add new url mapping
    def post(self, request):
        post_data = json.loads(request.body)
        url = post_data.get('url', None)
        if not url:
            return HttpResponseBadRequest()

        # TODO: url validation

        # create random charactors as short url id
        def short_id_creater(length, prefix=''):
            if len(prefix) < length:
                char_set_list = string.ascii_letters + string.digits
                for c in ''.join(random.sample(char_set_list, len(char_set_list))):
                    short_id = short_id_creater(length, prefix + c)
                    if short_id is not None:
                        return short_id
                return None

            elif len(prefix) == length:
                short_id = prefix
                obj, created = UrlMappingTable.objects.get_or_create(
                    pk=short_id,
                    defaults={'url': url},
                )
                if created:
                    return short_id
                else:
                    return None
            else:
                return None

        short_id = short_id_creater(settings.URL_LENGTH)
        if short_id is not None:
            context = dict(id=short_id)
            return JsonResponse(context)
        else:
            # all character combination are used
            return HttpResponseServerError()
