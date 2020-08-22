from django.urls import include, path


urlpatterns = ([
    path('', include('sochi_backend.event.urls')),
    path('users/', include('sochi_backend.users.urls', namespace="users-api")),
])
