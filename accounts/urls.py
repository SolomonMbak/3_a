from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),


#     path('accounts/password-reset/',
#          auth_views.PasswordResetView.as_view(), name='password_reset'),


#     path('accounts/password-reset/', auth_views.PasswordResetView.as_view(
#         template_name='accounts/password_reset_form.html'), name='password_reset'),


#     path('accounts/password-reset/done',
#          auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

#     path('accounts/password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

#     path('accounts/password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path("", views.index, name="index"),
    # path("about/", views.about, name="about"),
    # path("password-reset/", views.password_reset, name="password_reset"),
    # path("change_password/", views.change_password, name="change_password"),
    # path("account/login/", views.login_request, name="login"),
    # path("<single_slug>", views.single_slug, name="single_slug"),
    # path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    # path("terms/", views.terms, name="terms"),
    # path("publish_a_course/", views.publish_a_course, name="publish_a_course"),
]
