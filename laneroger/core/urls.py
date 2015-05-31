# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import ShowHomeView, SaveTheDateView, ConfirmacaoRedirectView


urlpatterns = patterns('',  # noqa

    url(r'^confirmacao/$', ConfirmacaoRedirectView.as_view(),
        name='core.confirmacao'),
    url(r'^confirmacao$',
        ConfirmacaoRedirectView.as_view(),),

    url(r'^$', ShowHomeView.as_view(),
        name='core.showhome'),

    url(r'^save-the-date/$',
        SaveTheDateView.as_view(), name='core.savethedate'),

    url(r'^dicasdehoteis/$',
        TemplateView.as_view(template_name="core/dicasdehoteis.html"),
        name='core.dicasdehoteis'),

    url(r'^cerimoniareligiosa/$',
        TemplateView.as_view(template_name="core/cerimoniareligiosa.html"),
        name='core.cerimoniareligiosa'),

)
