from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('list/', views.ListUserView.as_view(), name='list'),
    path('token/', views.CreateTokenViews.as_view(), name='token'),
    path('myprofile/', views.ManageUserView.as_view(), name='myprofile'),
]
