from rest_framework import routers

from crm.api.viewsets import *

router = routers.DefaultRouter()
router.register('crm', stockViewSet)
router.register('users', userViewSet, basename='user')
router.register('admin', adminViewSet, basename='admin')