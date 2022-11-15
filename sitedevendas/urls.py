from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from . import settings

from store.views import UserView , OrderView, CategoryView, ProductView, CustomerView, OneProductView


urlpatterns = [
path('admin/', admin.site.urls),
re_path(r'^category/$', CategoryView.as_view()),
re_path(r'^user/$', UserView.as_view()),
re_path(r'^order/$', OrderView.as_view()),
re_path(r'^product/$', ProductView.as_view()),
re_path(r'^customer/$', CustomerView.as_view()),
re_path(r'^product-one/$', OneProductView.as_view()),




#path('', include('store.urls'))
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)