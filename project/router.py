from rest_framework import routers

from crm.api.viewsets import *

router = routers.DefaultRouter()
router.register('crm', stockViewSet)