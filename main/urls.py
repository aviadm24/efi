"""efi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    path('project/add/', views.ProjCreate.as_view(), name='project_add'),
    path('project/<int:pk>/', views.ProjUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjDelete.as_view(), name='project_delete'),
    path('project_detail/add/', views.project_detailCreate.as_view(), name='project_detail_add'),
    path('project_detail/<int:pk>/', views.project_detailUpdate.as_view(), name='project_detail_update'),
    path('project_detail/<int:pk>/delete/', views.project_detailDelete.as_view(), name='project_detail_delete'),
    url(r'^thankyou$', TemplateView.as_view(template_name="main/thankyou.html"), name='thankyou'),
    url(r'^Proj_list$', views.ProjListView.as_view(), name='Proj_list'),
    url(r'^transfer_list$', views.TransferListView.as_view(), name='transfer_list'),
    path('project_list/<int:pk>', views.ProjectListView.as_view(), name='project_list'),
    path('edit_transfer/<int:pk>', views.transfer_update.as_view(), name='transfer_update'),
    path('delete_transfer/<int:pk>', views.transfer_delete.as_view(), name='transfer_delete'),
    url(r'^test_datetime$', TemplateView.as_view(template_name="main/test_datetime.html"), name='test_datetime'),
]
