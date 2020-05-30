from django.urls import path, include
from . import views
from .routers import router
app_name = 'account'

urlpatterns = [
    path('account/',include(router.urls)),
]
