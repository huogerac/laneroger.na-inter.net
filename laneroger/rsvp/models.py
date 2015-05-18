# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.db import models

from model_utils import Choices


class ConvidadoRSVP(models.Model):
    RSVP = Choices(('sim', _('Sim')),
                   ('nao', _('Não')), )
    data = models.DateTimeField(_('data'), auto_now_add=True)
    rsvp = models.CharField('Confirma presença?',
                            choices=RSVP, default=RSVP.sim,
                            max_length=16)
    nome_completo = models.CharField('nome completo', max_length=128)
    email = models.EmailField('e-mail', max_length=128, default='', blank=True)
    fone = models.CharField('fone', max_length=32, default='', blank=True)
    eh_primeiro_acesso = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Convidado RSVP")
        verbose_name_plural = _("Convidados (RSVP)")

    def __str__(self):
        return "{0} --> {1}".format(self.nome_completo, self.rsvp)


class AcompanhanteRSVP(models.Model):
    TIPO_ACOMPANHANTE = Choices(('adulto', _('Adulto')),
                                ('ate_8', _('Até 8 anos')), )
    convidado_rsvp = models.ForeignKey(ConvidadoRSVP,
                                       verbose_name=_('convidado'),
                                       related_name='acompanhantes')
    nome = models.CharField('nome', max_length=128)
    tipo = models.CharField('selecione', choices=TIPO_ACOMPANHANTE,
                            default=TIPO_ACOMPANHANTE.adulto,
                            max_length=16)

    class Meta:
        verbose_name = _("Acompanhante RSVP")
        verbose_name_plural = _("Acompanhantes (RSVP)")
        ordering = ('nome', )

    def __str__(self):
        return self.nome

    @property
    def tipo_verbose(self):
        return AcompanhanteRSVP.TIPO_ACOMPANHANTE[self.tipo]
