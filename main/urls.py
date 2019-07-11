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
    url(r'^login$', auth_views.login, name='login'),
    url(r'^$', views.main_list, name='main_list'),
    url(r'^main_list$', views.main_list, name='main_list'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^ended_projects$', views.ended_projects, name='ended_projects'),
    url(r'^staged_projects$', views.staged_projects, name='staged_projects'),
    url(r'^ajax/export_table/$', views.export_table, name='export_table'),
    # url(r'^to_send$', views.to_send, name='to_send'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^whole_list$', views.whole_list, name='whole_list'),
    # url(r'^table_view$', views.table_view, name='table_view'),
    url(r'^ajax/update_cell/$', views.update_cell_json, name='update_cell'),
    url(r'^ajax/stage_project/$', views.stage_project_json, name='stage_project'),
    url(r'^ajax/change_for_all_project_rows/$', views.change_for_all_project_rows, name='change_for_all_project_rows'),

    # url(r'^ajax/cancel_currency_fields/$', views.cancel_currency_fields, name='cancel_currency_fields'),

    url(r'^ajax/end_project/$', views.end_project_json, name='end_project'),
    url(r'^ajax/add_color/$', views.add_color_json, name='add_color'),
    url(r'^ajax/add_dollar/$', views.add_dollar, name='add_dollar'),
    url(r'^ajax/add_shekel/$', views.add_shekel, name='add_shekel'),
    url(r'^ajax/add_euro/$', views.add_euro, name='add_euro'),
    url(r'^test_datetime$', TemplateView.as_view(template_name="main/test_datetime.html"), name='test_datetime'),
]
