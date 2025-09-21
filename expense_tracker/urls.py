from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- import this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),
    path('', RedirectView.as_view(url='/expenses/')),  # <-- redirect root URL
]
