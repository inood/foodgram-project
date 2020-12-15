import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.flatpages import views

handler404 = "core.views.service.page_not_found"  # noqa
handler500 = "core.views.service.server_error"  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('core.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += [
    path('about-author/', views.flatpage, {'url': '/about-author/'},
         name='about'),
    path('about-spec/', views.flatpage, {'url': '/about-spec/'},
         name='terms'),
    path('contacts/', views.flatpage, {'url': '/contacts/'},
         name='contacts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
