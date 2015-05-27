from django.conf.urls import url, include
from rest_framework import routers
from userapp import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
	url(r'^user/signup', views.signup),
	url(r'^user/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include(router.urls)),
]
