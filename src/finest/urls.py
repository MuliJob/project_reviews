""" Finest app urls """
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from finest import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('members/login_user/', views.login_user, name='login'),
    path('members/logout_user/', views.logout_user, name='logout'),
    path('members/register_user', views.register_user, name='register_user'),
    path('user/<str:username>/', views.user_project_detail, name='user_detail'),
    path('accounts/google/login/callback/dashboard/overview/', views.dashboard, name='dashboard'),
    path('dashboard/explore/', views.explore, name='explore'),
    path('dashboard/my-reviews/', views.my_reviews, name='my_reviews'),
    path('dashboard/my-posts/', views.my_post, name='my_post'),
    path("dashboard/toggle-favorite/", views.toggle_favorite, name="toggle_favorite"),
    path('dashboard/favorites/', views.favorite, name='favorite'),
    path('dashboard/submit-website/', views.submit_website, name='submit_website'),
    path('dashboard/details/<int:pk>', views.my_post_detail, name='my_post_detail'),
    path('dashboard/all/details/<int:pk>', views.all_post_details, name='all_post_details'),
    path('dashboard/<int:pk>/add-review/', views.add_review, name='add_review'),
    path('dashboard/profile/<str:username>/', views.edit_profile, name='edit_profile'),
    path("follows/<str:author>/",views.follow_toggle, name="follow_toggle"),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('api/profiles/', views.ProfileListAPIView.as_view(), name='api_profiles'),
    path('api/projects/', views.SubmittedWebsiteListAPIView.as_view(), name='api_projects'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
