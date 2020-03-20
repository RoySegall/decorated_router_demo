from django.http import JsonResponse
from rest_framework.views import APIView
from decorated_router.api.decorators import url_decoration


@url_decoration(path="api/blog/")
class Blog(APIView):
    def get(self, request):
        return JsonResponse({'foo': 'bar'})
