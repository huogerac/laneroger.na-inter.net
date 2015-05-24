# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        to = self.request.GET.get("to")
        context = super(ShowHomeView, self).get_context_data(**kwargs)
        context['to'] = to
        return context


class SaveTheDateView(TemplateView):
    template_name = "core/savethedate.html"

    def get_context_data(self, **kwargs):
        to = self.request.GET.get("to") or "There"
        context = super(SaveTheDateView, self).get_context_data(**kwargs)
        context['to'] = to
        return context


class ConfirmacaoRedirectView(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        self.url = reverse('rsvp.confirmacaohome')
        return redirect(self.url)
