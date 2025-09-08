from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    # path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('job/', include('job.urls')),
    # path('contact/', include('contact.urls')),

)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

