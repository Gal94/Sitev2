from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), #tells the urls the pk is an int. detail view expects it a pk
    path('post/new/', views.PostCreateView.as_view(), name='post-create'), #expects the template name to be appname_form
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'), #expect a form template named post_confirm_delete

]

# looking for a template name -> <app>/<model>_<viewtype> -> blog/post_list.html