from django.urls import path
from django.contrib.auth import logout
from . import views


urlpatterns = [
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name= 'message_list'), #for get 
    path('api/messages/', views.message_list, name= 'message_list'),
    path('api/users/<int:pk>', views.users_list, name = 'users_list'), #for get 
    path('api/users/', views.users_list, name= 'users_list'), #for post
    path('', views.index, name= 'index'),
    path('register/', views.register_view, name= 'register'),
    path('chats/', views.chat_view, name= 'chats'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('logout/', views.logout, name= 'logout'),
]
    
