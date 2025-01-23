
from django.contrib import admin # type: ignore
from django.urls import path
from django.conf import settings
from django.conf.urls. static import static
from . import views

urlpatterns = [
    path('', views.list, name = 'tweet_list'),
    path('create/', views.create, name = 'tweet_create'),
       path('<int:tweet_id>/edit/', views.edit, name = 'tweet_edit'),
          path('<int:tweet_id>/delete/', views.delete, name = 'tweet_delete'),
           path('logout/', views.logout_view, name='logout'),
                path('login/', views.login2, name = 'login'),
             path('register/', views.register, name = 'register'),
                path('questions/', views.post_question, name='post_question'),
                  path('question/', views.listi, name='question'),
    path('questions/<int:id>/', views.question_detail, name='question_detail'),
    path('questions/<int:id>/reply/', views.reply_to_question, name='reply_to_question'),
    path('delete/<int:id>/', views.deleteques, name='delete'),
   path('del/<int:id>/', views.deleterep, name='deleteio'),
           
     

] 
