# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from .models import Presente, IntencaoDePresente


admin.site.register(Presente)
admin.site.register(IntencaoDePresente)
