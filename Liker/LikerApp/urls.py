from django.urls import path
from . import views

app_name='LikerApp'

urlpatterns=[
    path('',views.loginUser,name='loginUser'),
    path('signup/',views.register,name='signup'),
    path('login/',views.loginUser,name='loginUser'),
    path('profile/<str:pk>',views.profilePage,name="profile"),
    path('private_Post/<str:pk>/',views.personalPost,name='private_Post'),
    path('post/',views.publicPost,name='public_post'),
    path('createPost/<str:pk>/',views.createPost,name='create_post'),
    path('like/',views.like_post,name='like_post'),
    path('logout/',views.logoutUser,name='logout_user'),
    path('createComment/<str:pk>',views.comment_post,name='createComment'),
    path('displayComment/<str:pk>',views.display_comments,name='displayComment'),
    path('profile_pic/',views.customerSettings,name='settings'),
    path('specificPost/<str:pk>/',views.specificPost, name="specificPost"),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('changeUsername/',views.changeUsername,name="changeUsername"),
    path('settings/',views.settingsPage)
    ]
