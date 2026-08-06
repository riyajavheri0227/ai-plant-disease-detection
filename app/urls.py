from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('features/', views.features, name='features'),
    path('contacts/', views.contacts, name='contacts'),
    path("diseases/", views.diseases, name="diseases"),
    path("neem/", views.neem, name="neem"),
    path("tomato/", views.tomato, name="tomato"),
    path("sunflower/", views.sunflower, name="sunflower"),
    path("rose/", views.rose, name="rose"),
    path("papaya/", views.papaya, name="papaya"),
    path("mango/", views.mango, name="mango"),
    path("lotus/", views.lotus, name="lotus"),
    path("hibiscus/", views.hibiscus, name="hibiscus"),
    path("haldi/", views.haldi, name="haldi"),
    path("guava/", views.guava, name="guava"),
    path("coconut/", views.coconut, name="coconut"),
    path("banyan/", views.banyan, name="banyan"),
    path("banana/", views.banana, name="banana"),
    path("ashoka/", views.ashoka, name="ashoka"),
    path("aloe_vera/", views.aloe_vera, name="aloe_vera"),
    path("register/", views.register, name="register"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("scanplant/", views.scanplant, name="scanplant"),
    path("logout/", views.logout_user, name="logout"),
    path('myplants/', views.myplants, name='myplants'),
    path("add-myplant/<int:plant_id>/", views.add_myplant, name="add_myplant"),
    path("delete-myplant/<int:plant_id>/", views.delete_myplant, name="delete_myplant"),
    path("result/", views.result, name="result"),
   

]