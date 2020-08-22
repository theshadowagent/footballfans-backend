from django.urls import include, path

from sochi_backend.event.views import ListEventsView

urlpatterns = ([
    path('events', ListEventsView.as_view()),
    path('events/', include('sochi_backend.event.urls')),
    path('users/', include('sochi_backend.users.urls', namespace="users-api")),
])
