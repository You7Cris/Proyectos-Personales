from django.urls import path, include
from rest_framework import routers #Toma las vistas y las transforma en url
from tasks import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

# versionado de API
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API"))
]

# ''' GET
# POST
# PUT
# DELETE
# '''