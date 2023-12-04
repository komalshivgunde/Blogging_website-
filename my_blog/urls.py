from django.urls import path
from my_blog import views
from django.conf.urls.static import static
from blog import settings

urlpatterns = [
    path('home',views.home),
    path('register',views.register),
    path('login',views.user_login),
    path('header',views.header),
    path('footer',views.footer),
    path('readpost/<cat_id>',views.readpost),
    path('logout',views.user_logout),
    path('catfilter/<cat_id>',views.catfilter),
    path('save/<pid>',views.save),
    path('remove/<pid>',views.remove),
    path('viewsaved',views.viewsaved),
    path('about',views.about),
    path('contact',views.contact),
    path('post',views.post)
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)