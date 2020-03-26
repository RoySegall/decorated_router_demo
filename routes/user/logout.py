from django.http import JsonResponse
from django.views import View
from decorated_router.api.decorators import url_decoration


@url_decoration(path="api/user/logout/")
class Logout(View):
    def get(self, request):
        return JsonResponse({'foo': 'bar'})
