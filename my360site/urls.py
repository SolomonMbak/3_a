from django.contrib import admin
from django.urls import path, include
from contact.views import contact


admin.site.site_header = '360academia - Admin'
admin.site.index_title = '360academia - Admin'
admin.site.site_title = '360academia'


urlpatterns = [
    path('', include('main.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
