# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from model_report.views import report, report_list, report_list_for_app


urlpatterns = patterns('',
    url(r'^$', report_list, name='model_report_list'),
    url(r'^app/(?P<app>[\w-]+)/$', report_list_for_app, name='model_report_list_for_app'),
    url(r'^(?P<slug>[\w-]+)/$', report, name='model_report_view'),
)
