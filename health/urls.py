from django.urls import path
from. import views

urlpatterns=[
	path('', views.base, name='base'),
	path('index1/',views.index1, name='index1'),
	path('login/', views.login, name='login'),
]