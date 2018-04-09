from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^frontpage/', include('frontpage.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^singleproduct/', include('singleproduct.urls')),
    url(r'^admin/', admin.site.urls),
]
