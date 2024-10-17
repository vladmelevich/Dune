from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('blogers', views.blogers, name='blogers'),
    path('admin_m', views.admin, name='admin'),
    path('applications/', views.applications, name='applic'),
    path('applications_b/', views.applications_b, name='applic_b'),
    path('applications_m/', views.applications_m, name='applic_m'),
    path('blogers_manager', views.blogers_m, name='blogers_m'),
    path('bloger_info/<int:bloger_id>/', views.bloger_info, name= 'bloger_info'),
    path('post', views.post, name='post'),
    path('posts_m', views.posts_m, name='post_m'),
    path('profile_manager', views.profile_manager, name='profile_manager'),
    path('prof', views.prof, name='prof'),
    path('random/password', views.random_m, name='random'),
    path('result', views.result, name='result'),
    path('result/bloger', views.result_b, name='result_blog'),
    path('sign_up', views.reg, name='reg'),
    path('sign_in', views.auth, name='auth'),
    path('sign_in_men', views.auth_men, name='auth_men'),
    path('projects/', views.projects, name='projects'),
    path('projects_info/<int:projects_men_id>/', views.projects_info, name='projectsm_info'),
    path('projects_information/<int:projects_id>/', views.projects_information, name='projects_info'),
    path('projects_m/', views.projects_m, name='projects_m'),
    path('password-reset', PasswordResetView.as_view(
        template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')),
    name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')),
        name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]