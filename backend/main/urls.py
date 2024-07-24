from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from cards.urls import router as cards_urls

urlpatterns = [
                  path('api/v1/', include(cards_urls.urls)),
                  path('admin/', admin.site.urls),
              ] + staticfiles_urlpatterns()
