from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from snippets import views

# Multiple view classes are grouped together 
# & are connected to urls using routers.

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)


urlpatterns = [
    url('', include(router.urls))
]
