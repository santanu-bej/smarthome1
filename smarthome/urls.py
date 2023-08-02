from django.contrib import admin
from django.urls import path
from .views import get_switch_status,set_switch_status,add_switch,show_all_switches
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/switches/get/<str:switch_name>',view=get_switch_status),
    path('api/switches/set/<str:switch_name>',view=set_switch_status),
    path('api/switches/add/<str:switch_name>',view=add_switch),
    path('',view=show_all_switches),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
