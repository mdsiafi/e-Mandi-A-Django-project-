from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'efarm'
urlpatterns = [
    path('',views.index, name="index"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
    #path('welcome/farmer',views.welcomeFarmer, name="welcome_farmer"),
    #path('welcome/customer1',views.welcomeCustomer, name="welcome_customer1"),
    path('farmer/addcrop',views.addCrop, name="addcrop"),
    url(r'^(?P<object_id>[0-9]+)/delete_crop/$', views.cropDelete, name='delete_crop'),
    url(r'^crop/(?P<pk>\d+)/edit/$', views.EditCrop.as_view(), name="edit-crop"),
    #url(r'^crop/(?P<pk>\d+)/edit/$', views.EditCrop.as_view(), name="purchase-crop"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.crop_detail, name='crop_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.welcomeCustomer, name='crop_list_by_category'),
    url(r'^welcome/customer', views.welcomeCustomer, name='welcome_customer'),
    path('team',views.team, name="team"),
    url(r'^welcome/farmer/(?P<pk>\d+)/$', views.welcomeFarmer, name='welcome'),

]
