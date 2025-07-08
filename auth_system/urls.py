from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Добавьте этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Добавьте перенаправление с корневого URL на страницу входа
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]