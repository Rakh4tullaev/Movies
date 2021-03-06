from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("profile/", views.profile, name="profile"),
    path("profile/liked", views.liked, name="liked"),
    path("profile/watched", views.watched, name="watched"),
    path("profile/comments", views.comments, name="comments"),
    path('profile/movies/<slug:slug>/comments/<int:pk>/delete',
         views.profile_comment_delete, name='profile_comment_delete'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('users/<str:username>/',
         views.user_detail, name="user_detail_url"),
    path('users/<str:username>/liked', views.user_liked, name="user_liked"),
    path('users/<str:username>/watched',
         views.user_watched, name="user_watched"),
    path('users/<str:username>/comments',
         views.user_comments, name="user_comments"),
    path('movies/<slug:slug>/', views.movie_detail, name='movie_detail_url'),
    path('movies/<slug:slug>/comment/', views.comment, name='comment'),
    path('movies/<slug:slug>/comment/<int:pk>/like/', views.comment_like, name='comment_like'),
    path('movies/<slug:slug>/comment/<int:pk>/dislike/', views.comment_dislike, name='comment_dislike'),
    path('movies/<slug:slug>/comment/<int:pk>/delete',
         views.comment_delete, name='comment_delete'),
    path('movies/<slug:slug>/like/', views.like, name='like'),
    path('movies/<slug:slug>/dislike/', views.dislike, name='dislike'),
    path('genres/<slug:slug>/', views.genre_detail, name='genre_detail_url'),
    path('actors/<slug:slug>', views.actor_detail, name="actor_detail_url"),
    path('directors/<slug:slug>', views.director_detail,
         name="director_detail_url"),
    path('composers/<slug:slug>', views.composer_detail,
         name="composer_detail_url"),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path('sort/', views.sort, name="sort"),
    #     --------
    path('composers/<slug:slug>/ComposerFirstChoice',
         views.ComposerFirstChoice, name='ComposerFirstChoice'),
    path('composers/<slug:slug>/ComposerSecondChoice',
         views.ComposerSecondChoice, name='ComposerSecondChoice'),
    #     --------
    #     --------
    path('actors/<slug:slug>/firstChoice',
         views.firstChoice, name='firstChoice'),
    path('actors/<slug:slug>/secondChoice',
         views.secondChoice, name='secondChoice'),
    #     --------
    path('directors/<slug:slug>/DirectorFirstChoice',
         views.DirectorFirstChoice, name='DirectorFirstChoice'),
    path('directors/<slug:slug>/DirectorSecondChoice',
         views.DirectorSecondChoice, name='DirectorSecondChoice'),
    #     --------
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('terms-of-use', views.terms_of_use, name='terms_of_use')

]
