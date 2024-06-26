from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import send_test_email
urlpatterns = [
    path('', views.quote_list , name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('authors/', views.author_list, name='author_list'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('tags/<str:tag_name>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('scrape_quotes/', views.scrape_quotes, name='scrape_quotes'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('send_test_email/', send_test_email, name='send_test_email'),
]
