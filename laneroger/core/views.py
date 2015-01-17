# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
    	to = self.request.GET.get("to")
        context = super(ShowHomeView, self).get_context_data(**kwargs)
        context['to'] = to
        return context