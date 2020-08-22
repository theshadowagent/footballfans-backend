from django.urls import path

from sochi_backend.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view, UserEventCreateViewSet, UserTicketCreateViewSet, UserEventUpvoteViewSet,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),

    path('<int:u_id>/events/create', UserEventCreateViewSet.as_view({'post': 'create'})),
    path('<int:u_id>/events/like', UserEventUpvoteViewSet.as_view({'post': 'create'})),
    path('<int:u_id>/events/like/<int:event_id>/delete', UserEventUpvoteViewSet.as_view({'delete': 'destroy'})),
    path('<int:u_id>/tickets/create', UserTicketCreateViewSet.as_view({'post': 'create'})),
]
