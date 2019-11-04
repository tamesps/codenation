from django.urls import include, path

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'logs', views.LogApiViewSet)
router.register(r'origins', views.OriginApiViewSet)
router.register(r'levels', views.LevelApiViewSet)
router.register(r'users', views.UserApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('environments/',  views.EnvironmentListOnlyApiView.as_view()),
    path('token/',    views.UserToken.as_view()),
    path('signup/', views.SignUp),
]

