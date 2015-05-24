# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from .models import ConvidadoRSVP, AcompanhanteRSVP
from .forms import ConfirmacaoHomeForm, ConvidadoRSVPForm, AcompanhanteRSVPForm
from .validators import phone_validator


class ConfirmacaoHomeView(FormView):
    form_class = ConfirmacaoHomeForm
    success_url = "/rsvp/confirmado"
    template_name = "rsvp/confirmacaohome.html"

    def form_valid(self, form):
        fone, email = (form['fone'].data,
                       form['email'].data)

        fone = phone_validator(fone)
        email = email.lower()

        if email and fone:
            convidado = ConvidadoRSVP.objects.filter(email=email.lower(),
                                                     fone=fone)
        else:
            if email and ConvidadoRSVP.objects.filter(
                    email=email.lower()):
                convidado = ConvidadoRSVP.objects.filter(
                    email=email.lower())
            else:
                convidado = ConvidadoRSVP.objects.filter(fone=fone)

        if convidado:
            convidado = convidado[0]
        else:
            if email and fone:
                convidado, _ = ConvidadoRSVP.objects.get_or_create(
                    email=email, fone=fone)
            else:
                convidado, _ = ConvidadoRSVP.objects.get_or_create(
                    fone=fone)

        return HttpResponseRedirect(convidado.get_absolute_url())


class ConfirmacaoUpdateView(UpdateView):
    model = ConvidadoRSVP
    form_class = ConvidadoRSVPForm
    success_url = "/rsvp/confirmado"

    def get_context_data(self, **kwargs):
        context = super(ConfirmacaoUpdateView, self).get_context_data(**kwargs)
        context['acompanhante_form'] = AcompanhanteRSVPForm
        return context

    def form_valid(self, form):
        primeiro_acesso = self.object.eh_primeiro_acesso
        self.object = form.save(commit=False)
        self.object.eh_primeiro_acesso = False
        self.object.fone = phone_validator(self.object.fone)
        self.object.email = self.object.email.lower()
        self.object.save()
        if primeiro_acesso:
            return HttpResponseRedirect(self.object.get_absolute_url())
        return super(ConfirmacaoUpdateView, self).form_valid(form)


class ConfirmacaoAcompanhanteCreateView(CreateView):
    model = AcompanhanteRSVP
    form_class = AcompanhanteRSVPForm

    def form_valid(self, form):
        convidado = get_object_or_404(ConvidadoRSVP,
                                      pk=self.kwargs['convidado_pk'])
        self.object = form.save(commit=False)
        self.object.convidado_rsvp = convidado
        self.object.save()
        return HttpResponseRedirect(
            self.object.convidado_rsvp.get_absolute_url())


class ConfirmacaoAcompanhanteDeleteView(DeleteView):
    model = AcompanhanteRSVP
    form_class = AcompanhanteRSVPForm

    def get_success_url(self):
        convidado = get_object_or_404(ConvidadoRSVP,
                                      pk=self.kwargs['convidado_pk'])
        return convidado.get_absolute_url()
