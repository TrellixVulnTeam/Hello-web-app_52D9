from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about' ),
    url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services' ),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact' ),
    url(r'^profiles/(?P<slug>[-\w]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profiles/(?P<slug>[-\w]+)/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^admin/', admin.site.urls),
]
