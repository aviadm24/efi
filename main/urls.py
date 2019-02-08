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
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # url(r'^$', auth_views.login, name='login'),
    url(r'^$', views.main_list, name='main_list'),
    url(r'^main_list$', views.main_list, name='main_list'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^export_csv$', views.export_csv, name='export_csv'),
    url(r'^ajax/export_table/$', views.export_table, name='export_table'),
    url(r'^to_send$', views.to_send, name='to_send'),
    url(r'^ajax/export_filter/$', views.export_filter, name='export_filter'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^search_list$', views.search_list, name='search_list'),
    url(r'^p_num_list$', views.p_num_list, name='p_num_list'),
    url(r'^customer_list$', views.customer_list, name='customer_list'),
    url(r'^whole_list$', views.whole_list, name='whole_list'),
    url(r'^table_view$', views.table_view, name='table_view'),
    path('update_row/<int:pk>', views.update.as_view(), name='update_row'),
    url(r'^ajax/add_color/$', views.add_color_json, name='add_color'),
    url(r'^ajax/add_dollar/$', views.add_dollar, name='add_dollar'),
    url(r'^ajax/add_shekel/$', views.add_shekel, name='add_shekel'),
    url(r'^ajax/add_euro/$', views.add_euro, name='add_euro'),
    # url(r'^app/(?P<id>\d+)/new-page/$', views.myfunc, name="my_func"),
    # url(r'^$', views.add_to_main_list.as_view(), name='add_to_main_list'),
    # url(r'^$', views.homepage, name='homepage'),
    # path('project/add/', views.ProjCreate.as_view(), name='project_add'),
    # path('project/<int:pk>/', views.ProjUpdate.as_view(), name='project_update'),
    # path('project/<int:pk>/delete/', views.ProjDelete.as_view(), name='project_delete'),
    # path('project_detail/add/', views.project_detailCreate.as_view(), name='project_detail_add'),
    # path('project_detail/<int:pk>/', views.project_detailUpdate.as_view(), name='project_detail_update'),
    # path('project_detail/<int:pk>/delete/', views.project_detailDelete.as_view(), name='project_detail_delete'),
    # url(r'^thankyou$', TemplateView.as_view(template_name="main/thankyou.html"), name='thankyou'),
    # url(r'^Proj_list$', views.ProjListView.as_view(), name='Proj_list'),
    # url(r'^transfer_list$', views.TransferListView.as_view(), name='transfer_list'),
    # path('project_list/<int:pk>', views.ProjectListView.as_view(), name='project_list'),
    # path('edit_transfer/<int:pk>', views.transfer_update.as_view(), name='transfer_update'),
    #
    url(r'^test_datetime$', TemplateView.as_view(template_name="main/test_datetime.html"), name='test_datetime'),
]
