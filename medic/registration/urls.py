from django.urls import path
from . import views
urlpatterns = [
		path("register/", views.register, name = 'registration'),
		path('login/', views.user_login, name = 'login'),
		path("", views.home, name='home'),
		path('logout/', views.logouts, name= 'logout'),
		path('dashboard/', views.create_post, name= 'dashboard'),
		path('dashboard1/', views.dashboard1, name= 'dashboard'),
		path('zapys/', views.zapys, name = 'zapys'),

]
