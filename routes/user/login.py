from rest_framework.generics import GenericAPIView

from decorated_router.api.decorators import url_decoration


@url_decoration(path="api/user/login/")
class Login(GenericAPIView):
    def get(self, request):
        return 'login'
