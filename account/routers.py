from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('user',views.UserView)
router.register('profile',views.UserProfileView)