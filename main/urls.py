from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("our_courses/", views.our_courses, name="our_courses"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms/", views.terms, name="terms"),
    path("publish_a_course/", views.publish_a_course, name="publish_a_course"),
    
    # path("register/", views.register, name="register"),
    # path("account/", views.account, name="account"),
    # path("logout/", views.logout_request, name="logout"),
    # path("login/", views.login_request, name="login"),
    # path("password-reset/", views.password_reset, name="password_reset"),
    # path("change_password/", views.change_password, name="change_password"),
    # path("account/login/", views.login_request, name="login"),

    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(), name='password_reset'),


    # path('main/password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='main/password_reset_form.html'), name='password_reset'),


    # path('main/password-reset/done',
    #      auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # path('main/password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # path('main/password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
