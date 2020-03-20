from rest_framework.views import APIView
from django.views import View
from decorated_router.api.decorators import url_decoration


@url_decoration(path="api/user/logout/")
class Logout(View):
    def get(self, request):
        return 'logout'
