# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import ShowHomeView

urlpatterns = patterns('', 

    url(r'^$', ShowHomeView.as_view(), name='core.showhome'),

)
