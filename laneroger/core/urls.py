# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import ShowHomeView, SaveTheDateView, ConfirmacaoRedirectView


urlpatterns = patterns('',  # noqa

    url(r'^$', ShowHomeView.as_view(),
        name='core.showhome'),
    url(r'^confirmacao/$', ConfirmacaoRedirectView.as_view(),
        name='core.showhome'),
    url(r'^save-the-date/$',
        SaveTheDateView.as_view(), name='core.savethedate'),

)
