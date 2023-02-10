from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth_app/", include("auth_app.auth_urls")),
    path("ticket/", include("ticket.ticket_urls")),
    path("event/", include("event.event_urls")),
    path("prodact/", include("prodact.prodact_urls")),
]
