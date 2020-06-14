from django.urls import path, include
from . import views
from .routers import router
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'my_account'

urlpatterns = [
    path('account/',include(router.urls)),
    path('token/',obtain_jwt_token,name='obtain-token'),
    path('token/refresh',refresh_jwt_token,name='refresh-token'),
    path('token/verify',verify_jwt_token,name='verify-token'),
   
]
